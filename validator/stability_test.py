def run_stability_test(model_response: str) -> dict:
    """
    Test de stabilité cognitive initiale ou finale.
    Retourne un dictionnaire avec des indicateurs simples.
    """
    return {
        "coherence_score": len(model_response) % 10,  # Placeholder
        "consistency_flag": True
    }
