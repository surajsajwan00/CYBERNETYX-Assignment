from config import EMBEDDING_MODEL

def get_embeddings(text):
    return EMBEDDING_MODEL.encode(text).tolist()
