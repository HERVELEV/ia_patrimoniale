
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="RGPD – Consentement et gestion des données", layout="centered")
st.title("Protection des données personnelles (RGPD)")

st.markdown("**Ce module vous permet de respecter les obligations RGPD vis-à-vis de vos clients.**")

st.subheader("Consentement au traitement des données")
consent = st.checkbox("Je consens à ce que mes données soient collectées et traitées dans le cadre de cette mission de conseil patrimonial, conformément au RGPD.")

if consent:
    st.success("Consentement validé.")
else:
    st.warning("Le traitement des données ne peut commencer sans votre consentement.")

st.markdown("---")
st.subheader("Suppression de vos données")
nom = st.text_input("Nom du client à supprimer")

if st.button("Supprimer les données"):
    file_path = "data/client_data.csv"
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df_filtré = df[df["Nom"] != nom]
        df_filtré.to_csv(file_path, index=False)
        st.success(f"Toutes les données associées à {nom} ont été supprimées.")
    else:
        st.warning("Aucune base de données clients trouvée.")
