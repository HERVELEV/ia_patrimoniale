
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Collecte données client", layout="centered")
st.title("Collecte des données patrimoniales")

st.markdown("Merci de renseigner les informations suivantes pour établir votre profil patrimonial personnalisé.")

nom = st.text_input("Nom complet")
age = st.number_input("Âge", min_value=18, max_value=100)
revenu = st.number_input("Revenu annuel net (€)", step=1000)
patrimoine = st.number_input("Patrimoine total estimé (€)", step=10000)
objectif = st.selectbox("Objectif principal", ["Préparer la retraite", "Transmettre", "Optimiser la fiscalité", "Créer des revenus", "Diversifier le capital"])
profil_risque = st.radio("Profil de risque", ["Prudent", "Équilibré", "Dynamique"])

if st.button("Enregistrer les données"):
    data = {
        "Nom": nom,
        "Âge": age,
        "Revenu": revenu,
        "Patrimoine": patrimoine,
        "Objectif": objectif,
        "Profil": profil_risque
    }

    df = pd.DataFrame([data])
    if not os.path.exists("data"):
        os.makedirs("data")
    file_path = "data/client_data.csv"

    if os.path.exists(file_path):
        df.to_csv(file_path, mode='a', header=False, index=False)
    else:
        df.to_csv(file_path, index=False)

    st.success("Les données ont été enregistrées avec succès.")
