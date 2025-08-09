from typing import List, Dict, Any
import re


def chunk_text(
    text: str,
    chunk_size: int = 512,
    overlap: int = 200
) -> List[str]:
    """
    Splits text into overlapping chunks using tokens (word approximation).
    Args:
        text (str): The input text.
        chunk_size (int): Number of tokens per chunk.
        overlap (int): Number of overlapping tokens between chunks.
    Returns:
        List[str]: List of chunked strings.
    """
    # Simple whitespace/word tokenizer as a stand-in for real tokenization
    words = re.findall(r"\S+", text)
    chunks = []
    start = 0
    step = chunk_size - overlap
    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunk = ' '.join(words[start:end])
        chunks.append(chunk)
        if end == len(words):
            break
        start += step
    return chunks

def create_chunks_with_metadata(
    document: Dict[str, Any],
    chunk_size: int = 512,
    overlap: int = 200
) -> List[Dict[str, Any]]:
    """
    For a single document dict, returns a list of chunk dicts with inherited metadata.
    Document must have 'text', 'category', 'priority' and 'date' fields.
    """
    text = document['text']
    chunks = chunk_text(text, chunk_size=chunk_size, overlap=overlap)
    chunk_dicts = []
    for idx, chunk in enumerate(chunks):
        chunk_dict = {
            'chunk_text': chunk,
            'category': document.get('category', 'unknown'),
            'priority': document.get('priority', 'normal'),
            'date': document.get('date', None),
            'document_id': document.get('id', None),
            'chunk_index': idx
        }
        chunk_dicts.append(chunk_dict)
    return chunk_dicts
