from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_text(text):
    """
    Splits the extracted resume text into smaller meaningful chunks 
    for embedding and RAG retrieval.

    Args:
        text (str): The cleaned text extracted from PDF

    Returns:
        List[str]: List of text chunks
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,        # Maximum size of each chunk
        chunk_overlap=100,     # Overlap to maintain context
        separators=["\n\n", "\n", ".", " "]  # intelligent splitting
    )

    chunks = splitter.split_text(text)

    # Filter out empty or extremely small chunks
    chunks = [c.strip() for c in chunks if len(c.strip()) > 30]

    return chunks
