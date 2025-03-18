from fastapi import FastAPI
from app.model import summarize_text, ner, clean_text

app = FastAPI()

# Route racine
@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API de résumé de texte et NER !"}

# Route pour générer un résumé
@app.post("/summarize/")
def summarize(request: dict):
    text = clean_text(request["text"])
    try:
        summary = summarize_text(text)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la génération du résumé : {str(e)}")

# Route pour extraire les entités nommées
@app.post("/entity-recognition/")
def entity_recognition(request: dict):
    try:
        result = ner(request["text"])
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de l'extraction des entités : {str(e)}")