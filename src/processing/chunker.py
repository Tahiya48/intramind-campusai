from src.ingestion.document_schema import Document


def chunk_document(
    document: Document,
    chunk_size: int = 500,
    chunk_overlap: int = 100,
) -> list[Document]:
    """
    Split a document into overlapping text chunks while preserving metadata.
    """

    if not document.text:
        return []

    text = document.text
    chunks = []

    start = 0
    chunk_index = 0

    while start < len(text):
        end = min(start + chunk_size, len(text))

        # Prefer splitting at a space to avoid cutting words in half.
        if end < len(text):
            split_at = text.rfind(" ", start, end)

            if split_at > start:
                end = split_at

        chunk_text = text[start:end].strip()

        if chunk_text:
            chunks.append(
                Document(
                    text=chunk_text,
                    source=document.source,
                    document_type=document.document_type,
                    title=document.title,
                    page=document.page,
                    domain=document.domain,
                    chunk_index=chunk_index,
                )
            )

            chunk_index += 1

        # Move forward while preserving overlap.
        next_start = end - chunk_overlap

        # Prevent an infinite loop if the overlap is too large.
        if next_start <= start:
            next_start = end

        # Avoid starting the next chunk in the middle of a word.
        if next_start < len(text) and not text[next_start].isspace():
            next_space = text.find(" ", next_start)

            if next_space != -1:
                next_start = next_space + 1

        start = next_start

    return chunks