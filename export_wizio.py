
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Export vers Wizio", layout="centered")
st.title("Export des données clients vers Wizio (CSV)")

st.markdown("Ce module vous permet d'exporter les données du fichier client dans un format compatible avec Wizio.")

file_path = "data/client_data.csv"
if not os.path.exists(file_path):
    st.warning("Aucune base de données clients trouvée.")
else:
    df = pd.read_csv(file_path)

    # Mappage des colonnes vers format Wizio (exemple fictif, à adapter selon structure réelle)
    export_df = pd.DataFrame()
    export_df["Nom"] = df["Nom"]
    export_df["Email"] = ""  # À compléter dans collecte_donnees.py
    export_df["Téléphone"] = ""  # Idem
    export_df["Profil"] = df["Profil"] if "Profil" in df.columns else ""
    export_df["Objectif patrimonial"] = df["Objectif"]
    export_df["Revenus (€)"] = df["Revenu"]
    export_df["Patrimoine (€)"] = df["Patrimoine"]
    export_df["Commentaire IA"] = ""

    st.dataframe(export_df)

    if st.button("Exporter au format Wizio"):
        if not os.path.exists("exports"):
            os.makedirs("exports")
        export_path = "exports/export_wizio.csv"
        export_df.to_csv(export_path, index=False)
        st.success("Fichier export_wizio.csv généré avec succès.")
        with open(export_path, "rb") as f:
            st.download_button("Télécharger le fichier CSV", f, file_name="export_wizio.csv", mime="text/csv")
