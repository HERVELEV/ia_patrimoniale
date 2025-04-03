
import streamlit as st
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import os

st.set_page_config(page_title="OCR Document Upload", layout="centered")
st.title("Module OCR – Lecture automatique de documents")

uploaded_file = st.file_uploader("Téléversez un document (PDF ou image)", type=["pdf", "jpg", "jpeg", "png"])

if uploaded_file:
    st.info("Fichier reçu. Traitement en cours...")

    # Si c'est un PDF, le convertir en image(s)
    if uploaded_file.type == "application/pdf":
        with open("temp_doc.pdf", "wb") as f:
            f.write(uploaded_file.read())

        pages = convert_from_path("temp_doc.pdf", 300)
        st.image(pages[0], caption="Page 1 extraite", use_column_width=True)
        text = pytesseract.image_to_string(pages[0], lang="eng+fra")
        os.remove("temp_doc.pdf")

    else:
        image = Image.open(uploaded_file)
        st.image(image, caption="Image chargée", use_column_width=True)
        text = pytesseract.image_to_string(image, lang="eng+fra")

    st.subheader("Texte extrait du document :")
    st.code(text)
    st.success("Extraction OCR terminée.")
