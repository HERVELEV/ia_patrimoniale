
import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="Feedback IA", layout="centered")
st.title("Feedback sur les réponses de l'IA")

st.markdown("Veuillez évaluer la qualité de la réponse fournie par l'intelligence artificielle.")

client = st.text_input("Nom du client")
question = st.text_area("Question posée à l'IA")
reponse = st.text_area("Réponse fournie par l'IA")

utilite = st.radio("La réponse vous a-t-elle été utile ?", ["Oui", "Non"])
commentaire = st.text_area("Commentaire ou amélioration souhaitée")

if st.button("Envoyer le feedback"):
    horodatage = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    feedback_data = {
        "Nom": [client],
        "Question": [question],
        "Réponse IA": [reponse],
        "Utile": [utilite],
        "Commentaire": [commentaire],
        "Horodatage": [horodatage]
    }

    df = pd.DataFrame(feedback_data)
    if not os.path.exists("data"):
        os.makedirs("data")
    feedback_path = "data/feedback_ia.csv"
    if os.path.exists(feedback_path):
        df.to_csv(feedback_path, mode="a", header=False, index=False)
    else:
        df.to_csv(feedback_path, index=False)

    st.success("Merci pour votre retour. Le feedback a été enregistré.")
