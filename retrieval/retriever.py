from typing import List, Dict, Any
from retrieval.chroma_collection import get_or_create_collection


def retrieve_top_k(
    query: str,
    k: int = 5
) -> List[Dict[str, Any]]:
    """
    Retrieves top k most relevant chunks for a user query.
    Returns list of dicts each with 'chunk_text', 'category', 'priority', 'date', 'score'.
    """
    collection = get_or_create_collection()
    # Chroma expects list of queries
    results = collection.query(
        query_texts=[query],
        n_results=k,
        include=["metadatas", "documents", "distances"]
    )
    docs = results["documents"][0]
    metadatas = results["metadatas"][0]
    scores = results["distances"][0]
    # Lower distance = closer match (as using cosine)
    output = []
    for doc, meta, score in zip(docs, metadatas, scores):
        entry = {
            "chunk_text": doc,
            "category": meta.get("category", "unknown"),
            "priority": meta.get("priority", "normal"),
            "date": meta.get("date", None),
            "score": 1 - score,  # For cosine, 1-score is similarity
        }
        output.append(entry)
    return output
