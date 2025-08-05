import chromadb
from chromadb.config import Settings

client = chromadb.Client(Settings(anonymized_telemetry=False))
collection = client.get_or_create_collection("book_versions")

def save_version(text, version_id, metadata={}):
    collection.add(documents=[text], ids=[version_id], metadatas=[metadata])

def search_version(query):
    result = collection.query(query_texts=[query], n_results=1)
    return result['documents'][0][0] if result['documents'] else None
