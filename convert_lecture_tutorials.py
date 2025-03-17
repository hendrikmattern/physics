import os
import time
import base64
import mistune
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def md2html(input_md, output_html):
    """Converts Markdown to HTML using 'mistune' and adds MathJax."""
    try:
        with open(input_md, 'r', encoding='utf-8') as f:
            markdown_text = f.read()

        html_content = mistune.html(markdown_text)

        # Add MathJax script to the HTML
        mathjax_script = """
        <script>
            MathJax = {
                tex: {
                    inlineMath: [['$', '$']],
                    displayMath: [['$$', '$$']]
                },
                svg: {
                    fontCache: 'global'
                }
            };
        </script>
        <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
        """

        full_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Markdown to HTML</title>
        </head>
        <body>
            {html_content}
            {mathjax_script}
        </body>
        </html>
        """

        with open(output_html, 'w', encoding='utf-8') as f:
            f.write(full_html)

        print(f"HTML saved to {output_html}")

    except Exception as e:
        print(f"Error converting {input_md} to HTML: {e}")



def html2pdf(input_html, output_pdf):
    """Converts a single HTML file to a PDF using Selenium."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-software-rasterizer")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(f"file:///{os.path.abspath(input_html)}")

    # Wait for MathJax to finish processing
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

def convert_folder(input_folder):
    """Converts all Markdown files in a folder to PDFs via intermediate HTML."""
    for file in os.listdir(input_folder):
        if file.endswith(".md"):
            input_md = os.path.join(input_folder, file)
            output_html = os.path.join(input_folder, file.replace(".md", ".html"))
            output_pdf = os.path.join(input_folder, file.replace(".md", ".pdf"))

            # Convert Markdown to HTML
            md2html(input_md, output_html)

            # Convert HTML to PDF
            if os.path.exists(output_html):
                html2pdf(output_html, output_pdf)

# Define the target folder
base_path = os.getcwd()
lecture_tutorials_folder = os.path.join(base_path, "lecture_tutorials")

# Convert all Markdown files
convert_folder(lecture_tutorials_folder)
