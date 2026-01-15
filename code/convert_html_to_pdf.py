import os
import base64
from pathlib import Path
from typing import Iterable, List, Optional, Set

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import ChromiumOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

try:
    from selenium.webdriver.common.print_page_options import PrintOptions
    HAS_PRINT_OPTIONS = True
except Exception:
    HAS_PRINT_OPTIONS = False


# ---------- Chrome setup ----------

def build_chrome_options() -> ChromiumOptions:
    opts = webdriver.ChromeOptions()
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

def make_driver() -> webdriver.Chrome:
    service = Service(ChromeDriverManager().install(), log_path=os.devnull)
    return webdriver.Chrome(service=service, options=build_chrome_options())


# ---------- MathJax handling ----------

def wait_for_mathjax(driver: webdriver.Chrome, timeout_s: float = 15.0) -> None:
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


# ---------- Print helpers ----------

def build_print_settings():
    if HAS_PRINT_OPTIONS:
        po = PrintOptions()
        po.background = True
        po.landscape = False
        po.prefer_css_page_size = True
        return po
    else:
        return {
            "landscape": False,
            "displayHeaderFooter": False,
            "printBackground": True,
            "preferCSSPageSize": True,
        }

def print_to_pdf(driver: webdriver.Chrome, out_pdf: Path, settings) -> None:
    if HAS_PRINT_OPTIONS:
        pdf_base64 = driver.print_page(settings)
    else:
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
    """
    Accepts files and/or folders. From folders, collects files that:
      - match 'patterns' (glob), OR
      - have an allowed extension (default .html/.htm),
    and then (optionally) filters by substring 'contains' (case-insensitive).
    Deduplicates and returns a sorted list.
    """
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
            # Respect explicit file even if it doesn't match patterns/exts
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
        else:
            # path does not exist; ignore silently
            continue

    return sorted(out)


# ---------- Core API ----------

def html2pdf(driver: webdriver.Chrome, input_html: Path, output_pdf: Path) -> None:
    driver.get(input_html.resolve().as_uri())
    wait_for_mathjax(driver, timeout_s=15.0)
    settings = build_print_settings()
    print_to_pdf(driver, output_pdf, settings)

def convert_files(
    inputs: Iterable[Path],
    output_folder: Path,
    *,
    contains: Optional[str] = None,
    patterns: Optional[Iterable[str]] = None,
    recursive: bool = False,
) -> None:
    """
    Convert a mixed list of files/folders. Use 'contains' and/or 'patterns'
    to select from folders. Reuses one Chrome session for speed.
    """
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
    # Project root = parent of this script's directory
    script_dir = Path(__file__).resolve().parent
    base_path = script_dir.parent

    output_folder = base_path / "pdf_export"

    # Example inputs: mix of folders and individual files
    inputs = [
        base_path / "html_script",
        base_path / "html_slides",
        base_path / "html_lec_tut",
    ]

    # --- Choose ONE of the following usages ---

    # A) Filter by substring anywhere in filename (case-insensitive)
    convert_files(inputs, output_folder, contains="1_10")

    # B) Filter by glob pattern(s)
    # convert_files(inputs, output_folder, patterns=["*slides*.html", "*scripts*.html"])
