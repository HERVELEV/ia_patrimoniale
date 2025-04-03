
import streamlit as st
import os
import pandas as pd
from generation_documents import generate_documents_for_clients

st.set_page_config(page_title="Assistant IA Patrimonial", layout="centered")
st.title("Assistant IA – Tunnel Patrimonial Complet")

menu = [
    "Accueil",
    "Créer un compte CGP",
    "Dashboard CGP",
    "RGPD et consentement",
    "Collecte des données",
    "Générer les documents",
    "Consulter les données",
    "Catalogue Produits Partenaires",
    "Export vers Wizio",
    "Lecture de documents (OCR)",
    "Déclaration LCB-FT",
    "Vérification Gel des Avoirs",
    "Audit Trail",
    "Mémoire IA",
    "Recommandation IA personnalisée",
    "Feedback IA",
    "Génération du DDA",
    "Fusion dossier réglementaire",
    "Envoi de document à signer",
    "Réception signature (callback)"
]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Accueil":
    st.markdown("Bienvenue dans votre plateforme IA de gestion de patrimoine conforme CIF/AMF et RGPD.")

elif choice == "Créer un compte CGP":
    exec(open("onboarding_cgp.py").read())

elif choice == "Dashboard CGP":
    exec(open("tableau_de_bord_cgp.py").read())

elif choice == "RGPD et consentement":
    exec(open("rgpd_consentement.py").read())

elif choice == "Collecte des données":
    exec(open("collecte_donnees.py").read())

elif choice == "Générer les documents":
    st.subheader("Génération automatique des lettres de mission (brandées)")
    if st.button("Lancer la génération"):
        generate_documents_for_clients()
        st.success("Lettres générées avec succès.")

elif choice == "Consulter les données":
    if os.path.exists("data/client_data.csv"):
        df = pd.read_csv("data/client_data.csv")
        st.dataframe(df)
    else:
        st.warning("Aucune donnée client disponible.")

elif choice == "Catalogue Produits Partenaires":
    exec(open("catalogue_produits.py").read())

elif choice == "Export vers Wizio":
    exec(open("export_wizio.py").read())

elif choice == "Lecture de documents (OCR)":
    exec(open("ocr_module.py").read())

elif choice == "Déclaration LCB-FT":
    exec(open("lcbft_module.py").read())

elif choice == "Vérification Gel des Avoirs":
    exec(open("gel_avoirs.py").read())

elif choice == "Audit Trail":
    exec(open("audit_trail.py").read())

elif choice == "Mémoire IA":
    exec(open("memoire_ia_chroma.py").read())

elif choice == "Recommandation IA personnalisée":
    exec(open("recommandation_ai.py").read())

elif choice == "Feedback IA":
    exec(open("feedback_ia.py").read())

elif choice == "Génération du DDA":
    exec(open("dda_generator.py").read())

elif choice == "Fusion dossier réglementaire":
    exec(open("fusion_dossier_reglementaire.py").read())

elif choice == "Envoi de document à signer":
    exec(open("signature_api.py").read())

elif choice == "Réception signature (callback)":
    exec(open("callback_signature.py").read())
