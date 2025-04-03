
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="LCB-FT – Déclaration", layout="centered")
st.title("Lutte contre le blanchiment de capitaux et le financement du terrorisme (LCB-FT)")

file_path = "data/lcbft_data.csv"

st.markdown("Veuillez remplir les informations suivantes pour chaque client afin d'assurer votre conformité réglementaire.")

nom_client = st.text_input("Nom complet du client")
pep = st.radio("Le client est-il une personne politiquement exposée (PEP) ?", ["Non", "Oui"], index=0)
origine_fonds = st.selectbox("Origine principale des fonds investis", [
    "Salaires", "Héritage", "Revenus professionnels", "Vente d’actifs", "Dividendes", "Autre"
])
pays_residence = st.text_input("Pays de résidence fiscale")
pays_risque = ["Afghanistan", "Iran", "Corée du Nord", "Syrie", "Yémen", "Russie", "Soudan", "Cuba", "Haiti"]

justificatif = st.radio("Le client a-t-il fourni les justificatifs nécessaires ?", ["Oui", "Non"])

# Analyse de risque automatisée
risque = "Non"
if pep == "Oui" or justificatif == "Non" or pays_residence in pays_risque:
    risque = "Oui"

st.markdown(f"**Risque identifié :** {'A surveiller' if risque == 'Oui' else 'Non'}")

if st.button("Enregistrer cette déclaration LCB-FT"):
    data = {
        "Nom": [nom_client],
        "PEP": [pep],
        "Origine des fonds": [origine_fonds],
        "Pays fiscal": [pays_residence],
        "Justificatif fourni": [justificatif],
        "Risque identifié": [risque]
    }

    df = pd.DataFrame(data)
    if not os.path.exists("data"):
        os.makedirs("data")
    if os.path.exists(file_path):
        df.to_csv(file_path, mode="a", index=False, header=False)
    else:
        df.to_csv(file_path, index=False)

    st.success("Déclaration LCB-FT enregistrée avec succès.")
