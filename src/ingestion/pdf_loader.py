import pymupdf
from pathlib import Path


def extract_text_from_pdf(pdf_path: str) -> list[dict]:
    """
    Extract text from a PDF while preserving page-level metadata.

    Args:
        pdf_path: Path to the PDF file.

    Returns:
        A list of dictionaries containing page text and metadata.
    """

    pdf_file = Path(pdf_path)

    if not pdf_file.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    if pdf_file.suffix.lower() != ".pdf":
        raise ValueError("The provided file must be a PDF.")

    document = pymupdf.open(pdf_file)

    pages = []

    for page_number, page in enumerate(document, start=1):
        text = page.get_text("text").strip()

        if text:
            pages.append(
                {
                    "text": text,
                    "metadata": {
                        "source": pdf_file.name,
                        "page": page_number,
                    },
                }
            )

    document.close()

    return pages
