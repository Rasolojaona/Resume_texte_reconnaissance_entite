import streamlit as st
import requests

# URL de l'API FastAPI
API_URL = "http://127.0.0.1:8000"

# Titre de l'application
st.title("Application de Résumé et Reconnaissance d'Entités")

# Choix de la fonctionnalité
option = st.selectbox("Choisissez une fonctionnalité :", ["Résumé de texte", "Reconnaissance d'entités"])

# Fonction pour envoyer une requête à l'API
def send_request(endpoint, data):
    response = requests.post(f"{API_URL}/{endpoint}/", json=data)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Erreur : {response.text}")
        return None

# Interface pour le résumé de texte
if option == "Résumé de texte":
    st.subheader("Résumé de texte")
    input_text = st.text_area("Entrez le texte à résumer :")
    if st.button("Générer le résumé"):
        if input_text.strip():
            result = send_request("summarize", {"text": input_text})
            if result:
                st.success("Résumé généré :")
                st.write(result["summary"])
        else:
            st.warning("Veuillez entrer un texte.")

# Interface pour la reconnaissance d'entités
elif option == "Reconnaissance d'entités":
    st.subheader("Reconnaissance d'entités nommées")
    input_text = st.text_area("Entrez le texte à analyser :")
    if st.button("Extraire les entités"):
        if input_text.strip():
            result = send_request("entity-recognition", {"text": input_text})
            if result:
                st.success("Entités extraites :")
                for entity in result["entities"]:
                    st.write(f"- {entity['word']} ({entity['entity']})")
        else:
            st.warning("Veuillez entrer un texte.")