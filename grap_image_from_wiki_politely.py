import os
import requests
from bs4 import BeautifulSoup

def extract_and_format_license_md(soup):
    """
    Extracts license info from a Wikimedia Commons or Wikipedia file page soup.
    Returns a markdown-formatted attribution string, using strict matching priority.
    """

    def match_license(links, keywords):
        for a in links:
            href = a["href"].lower()
            for key in keywords:
                if key in href:
                    return a.get_text(strip=True), a["href"]
        return None, None

    # === Step 1: Structured license blocks ===
    license_blocks = soup.find_all("div", class_="licensetpl")

    for block in license_blocks:
        text = block.get_text(" ", strip=True).lower()
        links = block.find_all("a", href=True)

        if "cc by-sa 4.0" in text:
            _, url = match_license(links, ["by-sa/4.0"])
            if url: return f"[Attribution-Share Alike 4.0 International]({url})"
        elif "cc by-sa 3.0" in text:
            _, url = match_license(links, ["by-sa/3.0"])
            if url: return f"[Attribution-Share Alike 3.0 Unported]({url})"
        elif "cc by-sa 2.0" in text:
            _, url = match_license(links, ["by-sa/2.0"])
            if url: return f"[Attribution-Share Alike 2.0 Generic]({url})"
        elif "cc by-sa 1.0" in text:
            _, url = match_license(links, ["by-sa/1.0"])
            if url: return f"[Attribution-Share Alike 1.0 Generic]({url})"
        elif "cc by 2.0" in text:
            _, url = match_license(links, ["by/2.0"])
            if url: return f"[CC 2.0 Generic license]({url})"
        elif "gfdl" in text or "gnu free" in text:
            _, url = match_license(links, ["gnu.org"])
            return f"[GNU Free Documentation License]({url})" if url else "GNU Free Documentation License"
        elif "gemeinfrei" in text:
            return "gemeinfrei"
        elif "public domain" in text:
            return "public domain"
        elif "cc0" in text:
            _, url = match_license(links, ["publicdomain/zero/1.0"])
            return f"[CC0 1.0 Universal]({url})" if url else "CC0 1.0 Universal"

    # === Step 2: Table fallback for Wikipedia ===
    fileinfo_table = soup.find("table", class_="fileinfotpl")
    if fileinfo_table:
        for td in fileinfo_table.find_all("td"):
            text = td.get_text(" ", strip=True).lower()
            links = td.find_all("a", href=True)

            if "cc by-sa 3.0" in text:
                _, url = match_license(links, ["by-sa/3.0"])
                if url: return f"[Attribution-Share Alike 3.0 Unported]({url})"
            elif "cc by 2.0" in text:
                _, url = match_license(links, ["by/2.0"])
                if url: return f"[CC 2.0 Generic license]({url})"
            elif "gfdl" in text or "gnu free" in text:
                _, url = match_license(links, ["gnu.org"])
                return f"[GNU Free Documentation License]({url})" if url else "GNU Free Documentation License"
            elif "public domain" in text:
                return "public domain"
            elif "cc0" in text:
                _, url = match_license(links, ["publicdomain/zero/1.0"])
                return f"[CC0 1.0 Universal]({url})" if url else "CC0 1.0 Universal"

    # === Step 3: Search for plain-text public domain declarations ===
    body_text = soup.get_text(" ", strip=True).lower()
    if "i, the copyright holder of this work, release this work into the public domain" in body_text:
        return "public domain"

    # === Step 4: Fallback global link scan ===
    all_links = soup.find_all("a", href=True)
    for a in all_links:
        href = a["href"].lower()
        if "by-sa/4.0" in href:
            return f"[Attribution-Share Alike 4.0 International]({a['href']})"
        elif "by-sa/3.0" in href:
            return f"[Attribution-Share Alike 3.0 Unported]({a['href']})"
        elif "by-sa/2.0" in href:
            return f"[Attribution-Share Alike 2.0 Generic]({a['href']})"
        elif "by-sa/1.0" in href:
            return f"[Attribution-Share Alike 1.0 Generic]({a['href']})"
        elif "by/2.0" in href:
            return f"[CC 2.0 Generic license]({a['href']})"
        elif "gnu.org" in href:
            return f"[GNU Free Documentation License]({a['href']})"
        elif "publicdomain/zero/1.0" in href:
            return f"[CC0 1.0 Universal]({a['href']})"
        elif "gemeinfrei" in href:
            return "gemeinfrei"
        elif "publicdomain" in href:
            return "public domain"

    raise Exception("❌ License info not found or unsupported format.")


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
    "https://de.wikibooks.org/wiki/Datei:Spectral_lines_en.PNG",
    
]
for html in html_list: 
    print(f"Processing: {html}")
    download_wikipedia_image_no_convert(
        wiki_file_url=html,
        save_dir="img/from_wiki/",
        markdown_file="img/from_wiki/!license.md")
