import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def crawl_website(url):
    visited = set()
    texts = []

    domain = urlparse(url).netloc
    queue = [url]

    while queue:
        current_url = queue.pop(0)
        if current_url in visited:
            continue
        visited.add(current_url)

        try:
            response = requests.get(current_url, timeout=5)
            soup = BeautifulSoup(response.text, "html.parser")

            for tag in soup(["script", "style", "header", "footer", "nav", "aside"]):
                tag.decompose()

            text = soup.get_text(separator=" ", strip=True)
            if text:
                texts.append({
                    "content": text,
                    "source": current_url,
                    "title": soup.title.string if soup.title else ""
                })

            for link in soup.find_all("a", href=True):
                href = urljoin(url, link["href"])
                if urlparse(href).netloc == domain:
                    queue.append(href)
        except:
            continue

    return texts
