
import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="Vérification - Gel des avoirs", layout="centered")
st.title("Vérification du fichier gel des avoirs (LCB-FT)")

st.markdown("Selon les obligations LCB-FT, vous devez vérifier que le client ne figure pas sur la liste des personnes ou entités faisant l'objet d'une mesure de gel des avoirs en France.")

st.markdown("[Accéder au site officiel de vérification](https://gels-avoirs.dgtresor.gouv.fr)", unsafe_allow_html=True)
st.markdown("---")

nom = st.text_input("Nom et prénom du client à vérifier")
resultat = st.radio("Résultat de la recherche sur le site officiel :", ["Non inscrit", "Inscrit"])

if st.button("Valider et enregistrer la vérification"):
    if nom:
        horodatage = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        donnees = {
            "Nom": [nom],
            "Résultat vérification": [resultat],
            "Horodatage": [horodatage]
        }

        df = pd.DataFrame(donnees)
        if not os.path.exists("data"):
            os.makedirs("data")
        file_path = "data/gel_avoirs.csv"
        if os.path.exists(file_path):
            df.to_csv(file_path, mode="a", index=False, header=False)
        else:
            df.to_csv(file_path, index=False)

        st.success(f"Vérification enregistrée pour {nom} à {horodatage}")
    else:
        st.warning("Veuillez entrer le nom du client.")
