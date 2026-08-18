def expose_corpus() -> str:
    """
    Retourne le contenu du Corpus CATAR pour exposition au modèle.
    """
    with open("corpus/catar_corpus.txt", "r", encoding="utf-8") as f:
        return f.read()
