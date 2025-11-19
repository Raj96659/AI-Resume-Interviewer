import re

def clean_text(text: str) -> str:
    """
    Cleans raw PDF text for better chunking and embedding.

    Steps:
    - Remove extra spaces and newlines
    - Remove non-ASCII & weird symbols
    - Normalize spacing around punctuation
    - Remove repeated characters or formatting noise

    Args:
        text (str): Raw extracted text

    Returns:
        str: Clean, normalized text
    """

    if not text:
        return ""

    # Replace multiple newlines with a single newline
    text = re.sub(r"\n\s*\n+", "\n", text)

    # Remove multiple spaces
    text = re.sub(r"\s+", " ", text)

    # Remove non-printable symbols
    text = re.sub(r"[^\x00-\x7F]+", " ", text)

    # Fix spacing around punctuation
    text = re.sub(r"\s*([.,;:!?])\s*", r"\1 ", text)

    # Remove weird bullet points or unicode markers
    text = re.sub(r"[•●▪▪️■□-]{1}", " ", text)

    # Strip leading/trailing whitespace
    text = text.strip()

    return text
