from transformers import pipeline
from pydantic import BaseModel
import re
import numpy as np

summarizer = pipeline("summarization", model="facebook/bart-base")

# charger le modèle NER
ner_pipeline = pipeline('ner', model='dslim/bert-base-NER')

# clean text
def clean_text(text):
    """
    Nettoie le texte en supprimant les sauts à la ligne et les caractères spéciaux

    Args:
        text(str): Texte brute fourni par l'utilisateur

    Returns:
        str: Texte nettoyé
    """
    # Supprimer les espaces multiples
    text = re.sub(r"\s+", " ", text).strip()

    # Remplacer les sauts à la ligne par des espaces
    text = text.replace("\n", " ")
    
    # Échapper les caractères spéciaux si nécessaire
    text = text.replace('"', '\\"').replace("'", "\\'")
    
    return text

# fonction résumé de texte en francais
def summarize_text(text):
    """
    Résumé un texte donné en utilisant la pipeline de résumé

    Args:
        text(str): Texte à résumer.
        
    Returns:
        str: Résumé généré

    """
    summary = summarizer(text)
    return summary[0]['summary_text']


def clean_data(data):
    """
    Convertit les types incompatibles (comme numpy.float32) en types JSON compatibles.
    
    Args:
        data (list/dict): Données brutes générées par le modèle.
    
    Returns:
        list/dict: Données nettoyées.
    """
    if isinstance(data, list):
        return [clean_data(item) for item in data]
    elif isinstance(data, dict):
        return {key: clean_data(value) for key, value in data.items()}
    elif isinstance(data, np.float32):
        return float(data)  # Convertir numpy.float32 en float
    elif isinstance(data, np.int64):
        return int(data)    # Convertir numpy.int64 en int
    else:
        return data

def ner(input_text):
    """
    Identifie les entités nommées dans un texte donné.
    
    Args:
        input_text (str): Texte à analyser.
    
    Returns:
        dict: Un dictionnaire contenant le texte d'entrée et les entités extraites.
    """
    # Générer les entités nommées
    entities = ner_pipeline(input_text)
    
    # Nettoyer les données pour les rendre compatibles avec JSON
    cleaned_entities = clean_data(entities)
    
    # Retourner le résultat sous forme de dictionnaire
    return {"text": input_text, "entities": cleaned_entities}


# Modèle Pydantic pour valider les entrées
class SummarizationRequest(BaseModel):
    text: str
