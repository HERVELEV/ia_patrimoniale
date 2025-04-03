
import streamlit as st
from datetime import datetime
import os
import json

st.set_page_config(page_title="Callback Signature – Suivi", layout="centered")
st.title("Réception de la confirmation de signature électronique")

st.markdown("Ce module simule un endpoint de réception après signature électronique.")

# Simulation de payload de callback
exemple_payload = {
    "document_id": "12345",
    "client_email": "client@example.com",
    "signed_at": str(datetime.utcnow()),
    "status": "signed",
    "signature_platform": "Yousign"
}

st.subheader("Payload simulé de signature :")
st.json(exemple_payload)

if st.button("Simuler réception signature et archiver"):
    archive_dir = "archives_signatures"
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    filename = f"{archive_dir}/confirmation_signature_{exemple_payload['document_id']}.json"
    with open(filename, "w") as f:
        json.dump(exemple_payload, f, indent=4)

    st.success(f"Signature archivée dans : {filename}")
