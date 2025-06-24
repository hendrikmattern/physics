import os
import requests
from bs4 import BeautifulSoup

def extract_and_format_license_md(soup):
    """
    Extracts license info from the Wikipedia file page soup,
    returns a properly formatted markdown string for license attribution.
    """
    license_url = None
    license_text = None

    # Try to find the license div first
    license_div = soup.find("div", {"class": "fileinfotpl_license"})
    if license_div:
        a_tag = license_div.find("a", href=True)
        if a_tag:
            license_url = a_tag["href"]
            license_text = a_tag.get_text(strip=True)
        else:
            license_text = license_div.get_text(strip=True)

    # Fallback: search in entire page text or links if license info missing
    if not license_text:
        text = soup.get_text(separator=' ').lower()        
        if "cc0" in text:
            license_text = "CC0 1.0 Universal"
            license_url = "https://creativecommons.org/publicdomain/zero/1.0/deed.en"
        elif "public domain" in text:
            license_text = "public domain"
            license_url = None
        else:
            for a in soup.find_all("a", href=True):
                href = a["href"].lower()
                if "creativecommons.org/licenses" in href or "license" in href or "gnu" in href or "gfdl" in href:
                    license_url = a["href"]
                    license_text = a.get_text(strip=True)
                    break

    if not license_text:
        raise Exception("License info not found.")

    # Format license markdown text 
    if license_url:
        license_md = f"[{license_text}]({license_url})"
    else:
        license_md = f"{license_text}"

    return license_md

def download_wikipedia_image_no_convert(wiki_file_url, save_dir, markdown_file):
    print(f"Processing: {wiki_file_url}")

    # Fetch Wikipedia file page
    response = requests.get(wiki_file_url)
    if not response.ok:
        raise Exception(f"Failed to fetch page: {wiki_file_url}")
    soup = BeautifulSoup(response.text, "html.parser")

    # Find image URL with proper prefix handling
    file_div = soup.find("div", class_="fullImageLink")
    if not file_div:
        raise Exception("Image link not found on the page.")
    file_link = file_div.find("a")["href"]
    if file_link.startswith("//"):
        image_url = "https:" + file_link
    elif file_link.startswith("http"):
        image_url = file_link
    else:
        image_url = "https://en.wikipedia.org" + file_link

    image_name = os.path.basename(image_url)

    # Download image with User-Agent header
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Python requests"
    }
    image_response = requests.get(image_url, headers=headers)
    if not image_response.ok:
        raise Exception(f"Failed to download image: {image_url} Status code: {image_response.status_code}")

    # Ensure save directory exists
    os.makedirs(save_dir, exist_ok=True)
    image_path = os.path.join(save_dir, image_name)

    with open(image_path, "wb") as f:
        f.write(image_response.content)

    # Get formatted license markdown text using helper
    license_md = extract_and_format_license_md(soup)

    # Compose markdown
    md_entry = f"""
---

<img src="../img/from_wiki/{image_name}" alt="{image_name}" width="300"/>

*<sub>from [wikipedia]({wiki_file_url}), {license_md}</sub>*
"""
    # Ensure markdown directory exists
    md_dir = os.path.dirname(markdown_file)
    if md_dir and not os.path.exists(md_dir):
        os.makedirs(md_dir, exist_ok=True)

    with open(markdown_file, "a", encoding="utf-8") as f:
        f.write(md_entry)

    print(f"Downloaded and saved: {image_name}")
    print(f"Appended license info to: {markdown_file}")
    print(md_entry)


### MAIN EXECUTION

html_list = [
    "https://de.wikipedia.org/wiki/Datei:Lochkamera2.jpg",
    "https://commons.wikimedia.org/wiki/File:Kepschem-int.svg",
    "https://en.wikipedia.org/wiki/File:Pinhole-camera.svg",
    "https://en.wikipedia.org/wiki/File:Compound_microscope_geometric_optics.svg",    
    "https://en.wikipedia.org/wiki/File:Apochromat.svg",
    "https://en.wikipedia.org/wiki/File:Newtonian_telescope2.svg",
]
for html in html_list: 
    print(f"Processing: {html}")
    download_wikipedia_image_no_convert(
        wiki_file_url=html,
        save_dir="img/from_wiki/",
        markdown_file="img/from_wiki/!license.md")
