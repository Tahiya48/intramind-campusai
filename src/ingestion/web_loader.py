import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from src.ingestion.document_schema import Document


def extract_text_from_webpage(url: str) -> Document:
    """
    Extract useful text and metadata from a webpage.

    Args:
        url: URL of the webpage.

    Returns:
        A dictionary containing webpage text and metadata.
    """

    try:
        response = requests.get(
            url,
            timeout=15,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        response.raise_for_status()

    except requests.RequestException as error:
        raise RuntimeError(
            f"Unable to retrieve webpage: {url}"
        ) from error

    soup = BeautifulSoup(response.text, "html.parser")

    # Remove elements that usually contain navigation
    # or non-content information.
    for element in soup(
        ["script", "style", "nav", "footer", "header", "noscript"]
    ):
        element.decompose()

    text = soup.get_text(separator=" ", strip=True)

    title = soup.title.get_text(strip=True) if soup.title else ""

    domain = urlparse(url).netloc

    return Document(
        text=text,
        source=url,
        document_type="webpage",
        title=title,
        domain=domain,
    )