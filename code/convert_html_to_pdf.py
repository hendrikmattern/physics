import os
import base64
from pathlib import Path
from typing import Iterable, List, Optional, Set

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager


# ---------- Chrome setup ----------

def build_chrome_options() -> Options:
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--disable-software-rasterizer")
    opts.add_argument("--disable-notifications")
    opts.add_argument("--disable-background-networking")
    opts.add_argument("--allow-file-access-from-files")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_experimental_option("excludeSwitches", ["enable-logging"])
    opts.add_argument("--log-level=3")
    return opts


def make_driver() -> WebDriver:
    service = Service(ChromeDriverManager().install(), log_path=os.devnull)
    return webdriver.Chrome(service=service, options=build_chrome_options())


# ---------- MathJax handling ----------

def wait_for_mathjax(driver: WebDriver, timeout_s: float = 15.0) -> None:
    def mathjax_ready(drv):
        return drv.execute_script(
            "return (window.MathJax && typeof MathJax.typesetPromise === 'function') || false;"
        )

    try:
        WebDriverWait(driver, timeout_s, poll_frequency=0.25).until(mathjax_ready)
    except TimeoutException:
        return

    driver.execute_script("""
        if (!window.__mj_done) {
            window.__mj_done = false;
            MathJax.typesetPromise().then(function(){ window.__mj_done = true; });
        }
    """)

    try:
        WebDriverWait(driver, timeout_s, poll_frequency=0.25).until(
            lambda d: d.execute_script("return !!window.__mj_done;")
        )
    except TimeoutException:
        pass


# ---------- Slide overflow fix (CSS injection) ----------

def enforce_fit_width_for_slides(driver: WebDriver) -> None:
    """
    Defensive: make typical slide containers and images never exceed viewport width.
    This helps when content has fixed widths that would otherwise be cropped.
    """
    driver.execute_script(r"""
        if (!document.getElementById('__fit_width_css')) {
            const style = document.createElement('style');
            style.id = '__fit_width_css';
            style.textContent = `
                html, body { max-width: 100% !important; overflow-x: hidden !important; }
                img, svg, canvas, video { max-width: 100% !important; height: auto !important; }
                pre, code { max-width: 100% !important; overflow-wrap: anywhere !important; word-break: break-word !important; }
                table { max-width: 100% !important; }
                * { box-sizing: border-box !important; }
            `;
            document.head.appendChild(style);
        }
    """)


# ---------- Print helpers (CDP only) ----------

def build_print_settings(*, landscape: bool, scale: float = 1.0) -> dict:
    # Note: "scale" is supported by Chrome's Page.printToPDF.
    # shrinkToFit is generally honored when printing; we emulate this by using scale <= 1.0,
    # plus CSS constraints for slides. If your Chrome supports "shrinkToFit", you can add it too.
    settings = {
        "landscape": landscape,
        "displayHeaderFooter": False,
        "printBackground": True,
        "preferCSSPageSize": True,

        # Scale the rendering (0.1 .. 2.0). For wide slides, using < 1 helps prevent cropping.
        "scale": float(scale),

        # Optional: give Chrome a clear page box if your HTML doesn't define @page size.
        # These are in inches (A4 ~ 8.27 x 11.69).
        # Comment these out if you rely exclusively on CSS @page size.
        "paperWidth": 8.27,
        "paperHeight": 11.69,
    }
    return settings


def print_to_pdf(driver: WebDriver, out_pdf: Path, settings: dict) -> None:
    result = driver.execute_cdp_cmd("Page.printToPDF", settings)
    pdf_base64 = result["data"]
    out_pdf.parent.mkdir(parents=True, exist_ok=True)
    out_pdf.write_bytes(base64.b64decode(pdf_base64))


# ---------- File selection ----------

def collect_html_files(
    inputs: Iterable[Path],
    *,
    contains: Optional[str] = None,
    patterns: Optional[Iterable[str]] = None,
    recursive: bool = False,
    extensions: Iterable[str] = (".html", ".htm"),
) -> List[Path]:
    contains_lower = contains.lower() if contains else None
    exts = tuple(e.lower() for e in extensions)
    pats = list(patterns or [])
    seen: Set[Path] = set()
    out: List[Path] = []

    def maybe_add(p: Path):
        p = p.resolve()
        if not p.is_file():
            return
        if contains_lower and contains_lower not in p.name.lower():
            return
        if p not in seen:
            seen.add(p)
            out.append(p)

    for item in inputs:
        item = item.resolve()
        if item.is_file():
            maybe_add(item)
        elif item.is_dir():
            if pats:
                iters = []
                for pat in pats:
                    iters.append(item.rglob(pat) if recursive else item.glob(pat))
                for it in iters:
                    for p in it:
                        maybe_add(p)
            else:
                it = item.rglob("*") if recursive else item.glob("*")
                for p in it:
                    if p.is_file() and p.suffix.lower() in exts:
                        maybe_add(p)

    return sorted(out)


# ---------- Core API ----------

def html2pdf(driver: WebDriver, input_html: Path, output_pdf: Path) -> None:
    driver.get(input_html.resolve().as_uri())

    # Landscape only for files that contain ".slides" in the filename
    is_slides = ".slides" in input_html.name.lower()

    # If slides: enforce max-width constraints before printing (helps with fixed-width layouts)
    if is_slides:
        enforce_fit_width_for_slides(driver)

    wait_for_mathjax(driver, timeout_s=15.0)

    # If slides: use a slightly smaller scale to reduce the chance of cropping wide content.
    # You can tune 0.95 -> 0.9 if needed.
    scale = 0.95 if is_slides else 1.0

    settings = build_print_settings(landscape=is_slides, scale=scale)
    print_to_pdf(driver, output_pdf, settings)


def convert_files(
    inputs: Iterable[Path],
    output_folder: Path,
    *,
    contains: Optional[str] = None,
    patterns: Optional[Iterable[str]] = None,
    recursive: bool = False,
) -> None:
    files = collect_html_files(
        inputs, contains=contains, patterns=patterns, recursive=recursive
    )
    if not files:
        print("[info] No matching files found.")
        return

    with make_driver() as driver:
        for html in files:
            out_pdf = output_folder / (html.stem + ".pdf")
            try:
                html2pdf(driver, html, out_pdf)
                print(f"[ok] {html} -> {out_pdf}")
            except Exception as e:
                print(f"[fail] {html}: {e}")


# ---------- MAIN ----------

if __name__ == "__main__":
    script_dir = Path(__file__).resolve().parent
    base_path = script_dir.parent

    output_folder = base_path / "pdf_export"

    inputs = [
        base_path / "html_script",
        base_path / "html_slides",
        base_path / "html_lec_tut",
    ]

    #convert_files(inputs, output_folder, contains="1_10")
    convert_files(inputs, output_folder, contains=".slides")
