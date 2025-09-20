import spacy
from functools import lru_cache

@lru_cache(maxsize=1)
def get_nlp():
    return spacy.load("en_core_web_md")

def embed_text(word: str):
    nlp = get_nlp()
    doc = nlp(word)
    return doc.vector.tolist()
