from src.ingestion.pdf_loader import extract_text_from_pdf


pdf_path = "tests/sample_document.pdf"

pages = extract_text_from_pdf(pdf_path)


print(f"\nTotal pages extracted: {len(pages)}\n")

for page in pages:
    print("=" * 50)
    print(f"Source: {page.source}")
    print(f"Document type: {page.document_type}")
    print(f"Page: {page.page}")
    print("\nExtracted text:")
    print(page.text[:500])
    print()