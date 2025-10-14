import os
import time
import json
from urllib.parse import quote, unquote
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "FriendlyBot/1.0 (+https://example.org/contact) Python requests",
    "Accept-Language": "en;q=0.9,de;q=0.8",
}

def _get_with_retries(url, params=None, max_tries=3, timeout=20):
    for i in range(max_tries):
        try:
            r = requests.get(url, headers=HEADERS, params=params, timeout=timeout, allow_redirects=True)
        except requests.RequestException:
            r = None
        if r is not None and r.ok:
            return r
        time.sleep(2 * (i + 1))
    raise Exception(f"Failed to fetch after retries: {url}")

def _title_from_file_url(wiki_file_url: str) -> str:
    # Works for enwiki or commonswiki File:... pages
    if "/wiki/File:" not in wiki_file_url:
        raise ValueError("Not a File: page")
    title = wiki_file_url.split("/wiki/")[-1]   # "File:....svg"
    title = unquote(title).replace(" ", "_")
    return title

def fetch_commons_extmetadata(wiki_file_url: str):
    """
    Query Commons API for license + original URL. Returns dict:
    {
      "title": "File:...",
      "original_url": "...",
      "license_name": "...",
      "license_url": "...",
      "artist": "...",
      "credit": "..."
    }
    """
    title = _title_from_file_url(wiki_file_url)

    api = "https://commons.wikimedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "prop": "imageinfo",
        "titles": title,
        "iiprop": "url|extmetadata",
        "iiurlwidth": "0",
    }
    r = _get_with_retries(api, params=params, timeout=30)
    data = r.json()

    pages = data.get("query", {}).get("pages", {})
    if not pages:
        raise Exception("Commons API returned no pages")

    page = next(iter(pages.values()))
    if "imageinfo" not in page:
        raise Exception("Commons API: no imageinfo (file might not be on Commons)")

    ii = page["imageinfo"][0]
    meta = ii.get("extmetadata", {})

    license_name = meta.get("LicenseShortName", {}).get("value")
    license_url  = meta.get("LicenseUrl", {}).get("value")
    artist       = meta.get("Artist", {}).get("value")
    credit       = meta.get("Credit", {}).get("value")
    original_url = ii.get("url")

    return {
        "title": title,
        "original_url": original_url,
        "license_name": license_name,
        "license_url": license_url,
        "artist": artist,
        "credit": credit,
    }

def license_md_from_extmetadata(meta: dict) -> str:
    name = meta.get("license_name")
    url  = meta.get("license_url")
    if name and url:
        return f"[{name}]({url})"
    if name:
        return name
    if url:
        return f"[License]({url})"
    return "License: unknown"

def extract_and_format_license_md(soup):
    """
    Your original fallback license scraper.
    """
    def match_license(links, keywords):
        for a in links:
            href = a["href"].lower()
            for key in keywords:
                if key in href:
                    return a.get_text(strip=True), a["href"]
        return None, None

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

    body_text = soup.get_text(" ", strip=True).lower()
    if "i, the copyright holder of this work, release this work into the public domain" in body_text:
        return "public domain"

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

    # Fetch HTML page (needed for fallback + context)
    page_resp = requests.get(
        wiki_file_url,
        headers=HEADERS,
        timeout=20,
        allow_redirects=True,
    )
    if not page_resp.ok:
        print("status:", page_resp.status_code, page_resp.reason)
        print("final_url:", page_resp.url)
        print("first 300 chars:", page_resp.text[:300])
        raise Exception(f"Failed to fetch page: {wiki_file_url}")
    soup = BeautifulSoup(page_resp.text, "html.parser")

    # --- 1) Try Commons API ---
    image_url = None
    license_md = None
    try:
        meta = fetch_commons_extmetadata(wiki_file_url)
        image_url = meta.get("original_url")
        license_md = license_md_from_extmetadata(meta)
    except Exception as e:
        pass

    # --- 2) Fallback DOM parsing ---
    if not image_url:
        full_media = soup.find("div", class_="fullMedia")
        if full_media:
            a = full_media.find("a", class_="internal", href=True)
            if a:
                href = a["href"]
                image_url = ("https:" + href) if href.startswith("//") else href
        if not image_url:
            file_div = soup.find("div", class_="fullImageLink")
            if file_div:
                a = file_div.find("a", href=True)
                if a:
                    href = a["href"]
                    if href.startswith("//"):
                        image_url = "https:" + href
                    elif href.startswith("http"):
                        image_url = href
                    else:
                        image_url = "https://en.wikipedia.org" + href
        if not image_url and "/wiki/File:" in wiki_file_url:
            title = wiki_file_url.split("/wiki/")[-1].replace("File:", "")
            image_url = f"https://commons.wikimedia.org/wiki/Special:FilePath/{quote(title)}"

    if not image_url:
        raise Exception("Image link not found via API or page DOM.")

    image_name = os.path.basename(image_url.split("?")[0])

    # Download image
    img_resp = _get_with_retries(image_url, timeout=60)
    if not img_resp.ok:
        raise Exception(f"Failed to download image: {image_url} Status code: {img_resp.status_code}")

    os.makedirs(save_dir, exist_ok=True)
    image_path = os.path.join(save_dir, image_name)
    with open(image_path, "wb") as f:
        f.write(img_resp.content)

    # License fallback
    if not license_md:
        try:
            license_md = extract_and_format_license_md(soup)
        except Exception:
            license_md = "License: unknown"

    # Compose markdown
    md_entry = f"""
---

<img src="../img/from_wiki/{image_name}" alt="{image_name}" width="300"/>

*<sub>from [wikipedia]({wiki_file_url}), {license_md}</sub>*
"""
    md_dir = os.path.dirname(markdown_file)
    if md_dir and not os.path.exists(md_dir):
        os.makedirs(md_dir, exist_ok=True)

    with open(markdown_file, "a", encoding="utf-8") as f:
        f.write(md_entry)

    print(f"Downloaded and saved: {image_name}")
    print(f"Appended license info to: {markdown_file}")
    print(md_entry)

### MAIN EXECUTION
if __name__ == "__main__":

    # determine project root (one level up from /code)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(script_dir, ".."))

    # construct absolute paths relative to project root
    save_dir = os.path.join(project_root, "img", "from_wiki")
    markdown_file = os.path.join(save_dir, "!license.md")

    # define htmls
    html_list = [
        "https://en.wikipedia.org/wiki/File:Wikipage_pic.PNG",
        "https://en.wikipedia.org/wiki/File:Distancedisplacement.svg"
    ]
  
    # loop and download
    for html in html_list:
        download_wikipedia_image_no_convert(
            wiki_file_url=html,
            save_dir=save_dir,
            markdown_file=markdown_file
        )
