from src.ingestion.web_loader import extract_text_from_webpage


url = "http://localhost:8000/student-services.html"
document = extract_text_from_webpage(url)


print("\nWebpage successfully extracted!\n")

print("=" * 50)
print(f"Title: {document.title}")
print(f"Source: {document.source}")
print(f"Domain: {document.domain}")
print(f"Document type: {document.document_type}")

print("\nExtracted text:")
print(document.text[:1000])