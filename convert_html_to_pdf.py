import os
import base64
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def html2pdf(input_html, output_pdf):
    """Converts a single HTML file to a PDF."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-software-rasterizer")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(f"file:///{os.path.abspath(input_html)}")
    
    # Wait for MathJax to finish processing
    mathjax_loaded = False
    for _ in range(30):  # 15 seconds max
        mathjax_loaded = driver.execute_script("""
            if (window.MathJax) {
                return MathJax.typesetPromise ? true : false;
            }
            return false;
        """)
        if mathjax_loaded:
            break
        time.sleep(0.5)
    
    if mathjax_loaded:
        driver.execute_script("MathJax.typesetPromise()")
        time.sleep(2)  # Ensure rendering is complete
    
    settings = {
        "landscape": False,
        "displayHeaderFooter": False,
        "printBackground": True,
        "preferCSSPageSize": True,
    }
    
    result = driver.execute_cdp_cmd("Page.printToPDF", settings)
    
    with open(output_pdf, "wb") as f:
        f.write(base64.b64decode(result['data']))
    
    driver.quit()
    print(f"PDF saved to {output_pdf}")

def convert_folder(input_folder, output_folder):
    """Converts all HTML files in a folder to PDFs."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for file in os.listdir(input_folder):
        if file.endswith(".html"):
            input_html = os.path.join(input_folder, file)
            output_pdf = os.path.join(output_folder, file.replace(".html", ".pdf"))
            html2pdf(input_html, output_pdf)


base_path = os.getcwd()
output_folder = os.path.join(base_path, "pdf_export")

folders = ["html_script", "html_slides"]

for folder in folders:
    input_folder = os.path.join(base_path, folder)
    convert_folder(input_folder, output_folder)
