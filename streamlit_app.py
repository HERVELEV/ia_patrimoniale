
import streamlit as st
import zipfile
import os
import shutil
import subprocess

st.set_page_config(page_title="Déploiement IA Patrimoniale", layout="centered")
st.title("🚀 Déploiement IA Patrimoniale")

uploaded_file = st.file_uploader("Sélectionne ton fichier .zip contenant l'application :", type="zip")

if uploaded_file:
    zip_filename = uploaded_file.name
    zip_save_path = os.path.join(".", zip_filename)

    with open(zip_save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    project_name = os.path.splitext(zip_filename)[0]
    st.success(f"Fichier {zip_filename} téléchargé avec succès.")

    if st.button("📦 Déployer maintenant en local (terminal)"):
        st.warning("💡 Lancement manuel requis depuis ton terminal Windows avec le script 'lancer_local.bat'.")
