# app/utils.py
import nltk
from evaluate import load

# Télécharger les ressources NLTK nécessaires
nltk.download("punkt")

# Charger la métrique ROUGE pour l'évaluation
rouge_metric = load("rouge")

def evaluate_summary(reference, prediction):
    """
    Évalue un résumé généré par rapport à un résumé de référence.
    """
    results = rouge_metric.compute(predictions=[prediction], references=[reference])
    return results