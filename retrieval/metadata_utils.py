from typing import Dict, Any
import datetime

def enrich_metadata(
    chunk: Dict[str, Any],
    doc_metadata: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Ensure each chunk has required metadata fields, standardizing category, priority, and date.
    """
    chunk['category'] = doc_metadata.get('category', 'unknown')
    chunk['priority'] = doc_metadata.get('priority', 'normal')
    raw_date = doc_metadata.get('date', None)
    if raw_date:
        try:
            dt = datetime.datetime.fromisoformat(raw_date)
            chunk['date'] = dt.isoformat()
        except Exception:
            chunk['date'] = '1970-01-01T00:00:00'
    else:
        chunk['date'] = '1970-01-01T00:00:00'
    return chunk
