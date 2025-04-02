
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

    if st.button("📦 Lancer le déploiement vers GitHub"):
        try:
            # Supprimer l'ancien dossier si besoin
            if os.path.exists(project_name):
                shutil.rmtree(project_name)

            with zipfile.ZipFile(zip_save_path, 'r') as zip_ref:
                zip_ref.extractall(".")

            st.info("✅ Décompression terminée. Initialisation Git en cours...")

            # Appel du script PowerShell
            result = subprocess.run(
                ["powershell", "-ExecutionPolicy", "Bypass", "-File", "lancer_deploiement.ps1", project_name],
                capture_output=True, text=True
            )

            if result.returncode == 0:
                st.success("🚀 Déploiement GitHub terminé avec succès !")
            else:
                st.error(f"❌ Échec du script PowerShell. Code {result.returncode}")
                st.code(result.stderr)
        except Exception as e:
            st.error(f"❌ Erreur lors du traitement : {e}")
