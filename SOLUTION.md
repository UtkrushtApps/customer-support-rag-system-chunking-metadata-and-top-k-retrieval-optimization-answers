# Solution Steps

1. Implement `chunking.py` with a function to split documents into overlapping (200-token overlap) chunks and attach key metadata (category, priority, date) to each chunk.

2. Implement `metadata_utils.py` to standardize and ensure each chunk carries the correct and normalized metadata fields.

3. In `chroma_collection.py`, create or connect to the Chroma collection using cosine similarity and optimized ANN (HNSW) search parameters for high recall and low latency, and ensure embedding function is specified.

4. In `retriever.py`, implement the retrieval function that queries the Chroma collection, retrieves the top-5 most relevant chunks including their text and metadata, and returns results in an enriched format.

5. Ensure that all retrieved chunks include the fields: chunk_text, category, priority, date, and similarity score, ready for evaluation and FastAPI usage.

