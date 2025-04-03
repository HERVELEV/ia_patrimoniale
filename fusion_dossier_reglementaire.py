
from PyPDF2 import PdfMerger
import os
import streamlit as st

st.set_page_config(page_title="Fusion Dossier Réglementaire", layout="centered")
st.title("Fusion du dossier réglementaire (DER, LM, KYC, etc.)")

client_nom = st.text_input("Nom complet du client (sans accents)")

# Dossier contenant les documents PDF
pdf_dir = "generated_pdfs"

# Noms de fichiers attendus
documents = [
    f"DER_{client_nom}.pdf",
    f"lettre_mission_{client_nom}.pdf",
    f"KYC_{client_nom}.pdf",
    f"CEX_{client_nom}.pdf",
    f"LCBFT_{client_nom}.pdf"
]

if st.button("Fusionner les documents en un seul PDF"):
    merger = PdfMerger()
    missing_files = []

    for doc in documents:
        path = os.path.join(pdf_dir, doc)
        if os.path.exists(path):
            merger.append(path)
        else:
            missing_files.append(doc)

    if missing_files:
        st.warning(f"Les fichiers suivants sont manquants : {', '.join(missing_files)}")
    else:
        output_file = os.path.join("generated_pdfs", f"dossier_reglementaire_{client_nom}.pdf")
        merger.write(output_file)
        merger.close()
        st.success("Fichier fusionné avec succès.")
        with open(output_file, "rb") as f:
            st.download_button("Télécharger le dossier réglementaire", f, file_name=os.path.basename(output_file), mime="application/pdf")
