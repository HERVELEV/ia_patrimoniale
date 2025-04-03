
import streamlit as st
import pandas as pd
from fpdf import FPDF
import os

st.set_page_config(page_title="Génération du DDA", layout="centered")
st.title("Rapport d'adéquation (DDA) – Génération automatique")

file_path = "data/client_data.csv"
if not os.path.exists(file_path):
    st.warning("Aucune donnée client disponible.")
else:
    df = pd.read_csv(file_path)
    selected_client = st.selectbox("Choisir un client", df["Nom"].unique())

    client_data = df[df["Nom"] == selected_client].iloc[0]
    recommandation = st.text_area("Copiez ici la recommandation IA générée", height=250)

    if st.button("Générer le DDA PDF"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 10, "Document d’Adéquation (DDA)", ln=True, align="C")
        pdf.ln(10)

        pdf.set_font("Arial", "", 12)
        pdf.multi_cell(0, 8, f"Client : {client_data['Nom']}")
        pdf.multi_cell(0, 8, f"Âge : {client_data['Âge']}")
        pdf.multi_cell(0, 8, f"Profil de risque : {client_data['Profil']}")
        pdf.multi_cell(0, 8, f"Objectif : {client_data['Objectif']}")
        pdf.multi_cell(0, 8, f"Revenu annuel : {client_data['Revenu']} €")
        pdf.multi_cell(0, 8, f"Patrimoine estimé : {client_data['Patrimoine']} €")
        pdf.ln(5)
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "Stratégie recommandée :", ln=True)
        pdf.set_font("Arial", "", 11)
        pdf.multi_cell(0, 8, recommandation)

        if not os.path.exists("generated_pdfs"):
            os.makedirs("generated_pdfs")
        pdf_path = f"generated_pdfs/DDA_{client_data['Nom'].replace(' ', '_')}.pdf"
        pdf.output(pdf_path)

        st.success(f"DDA généré : {pdf_path}")
        with open(pdf_path, "rb") as f:
            st.download_button("Télécharger le DDA", f, file_name=os.path.basename(pdf_path), mime="application/pdf")
