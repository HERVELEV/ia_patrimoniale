
import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="Audit Trail", layout="centered")
st.title("Journal d'audit (Audit Trail réglementaire)")

st.markdown("Ce module permet de tracer toutes les étapes effectuées pour chaque client, avec horodatage complet.")

client = st.text_input("Nom du client concerné")

evenement = st.selectbox("Événement à enregistrer", [
    "Consentement RGPD",
    "Création fiche client",
    "Génération lettre de mission",
    "Déclaration LCB-FT",
    "Vérification Gel des avoirs",
    "Génération DDA",
    "Signature électronique envoyée",
    "Signature électronique reçue",
    "Fusion dossier réglementaire",
    "Export vers Wizio"
])

details = st.text_area("Commentaire complémentaire (optionnel)")

if st.button("Enregistrer l’événement"):
    horodatage = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_data = {
        "Nom": [client],
        "Événement": [evenement],
        "Détail": [details],
        "Horodatage": [horodatage]
    }

    df_log = pd.DataFrame(log_data)
    if not os.path.exists("data"):
        os.makedirs("data")
    log_path = f"data/audit_trail.csv"

    if os.path.exists(log_path):
        df_log.to_csv(log_path, mode="a", header=False, index=False)
    else:
        df_log.to_csv(log_path, index=False)

    st.success(f"Événement '{evenement}' enregistré pour {client} à {horodatage}.")
