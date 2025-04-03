
import requests
import streamlit as st

st.set_page_config(page_title="Signature électronique", layout="centered")
st.title("Signature électronique des documents")

# Formulaire pour récupérer l'email et le PDF
email = st.text_input("Email du client")
pdf_path = st.text_input("Nom du fichier PDF (dans /generated_pdfs)")

# Paramètres de la plateforme de signature (exemple avec Yousign)
api_url = "https://api.yousign.com/v1/signatures"
api_key = st.secrets["YOUSIGN_API_KEY"] if "YOUSIGN_API_KEY" in st.secrets else "ton_api_key"
redirect_url = "https://votre.site.com/confirmation"  # URL de confirmation après la signature

def envoyer_document_pour_signature(email, fichier_pdf):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    # Création de la demande de signature
    payload = {
        "documents": [
            {
                "document_url": f"/generated_pdfs/{fichier_pdf}",
                "signature_order": 1
            }
        ],
        "signers": [
            {
                "email": email,
                "first_name": "Client",  # Personnaliser avec le prénom du client
                "last_name": "Nom",      # Personnaliser avec le nom du client
            }
        ],
        "redirect_url": redirect_url,
        "message": "Merci de signer le document"
    }

    response = requests.post(api_url, headers=headers, json=payload)

    if response.status_code == 200:
        st.success("Document envoyé pour signature.")
        st.write(response.json())
    else:
        st.error("Erreur lors de l'envoi pour signature.")
        st.write(response.text)

if st.button("Envoyer pour signature électronique"):
    if email and pdf_path:
        envoyer_document_pour_signature(email, pdf_path)
    else:
        st.warning("Veuillez fournir un email et un fichier PDF valide.")
