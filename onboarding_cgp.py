
import streamlit as st
import os
import pandas as pd
import hashlib
from datetime import datetime

st.set_page_config(page_title="Onboarding CGP", layout="centered")
st.title("Création d'un compte CGP (Marque Blanche)")

st.markdown("Remplissez ce formulaire pour créer un compte utilisateur CGP et initialiser votre environnement.")

prenom = st.text_input("Prénom")
nom = st.text_input("Nom")
email = st.text_input("Email professionnel")
cabinet = st.text_input("Nom de votre cabinet")
mot_de_passe = st.text_input("Mot de passe", type="password")

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

if st.button("Créer mon compte"):
    if prenom and nom and email and cabinet and mot_de_passe:
        hashed_pw = hash_password(mot_de_passe)
        user_id = f"{prenom.lower()}_{nom.lower()}"

        user_data = {
            "Nom complet": [f"{prenom} {nom}"],
            "Email": [email],
            "Cabinet": [cabinet],
            "ID utilisateur": [user_id],
            "Mot de passe chiffré": [hashed_pw],
            "Date création": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
        }

        df_user = pd.DataFrame(user_data)

        if not os.path.exists("users"):
            os.makedirs("users")
        user_file = "users/users.csv"

        if os.path.exists(user_file):
            df_user.to_csv(user_file, mode="a", header=False, index=False)
        else:
            df_user.to_csv(user_file, index=False)

        # Créer environnement personnel
        cgp_path = f"data/cgp_{user_id}"
        os.makedirs(cgp_path, exist_ok=True)

        st.success(f"Compte CGP créé avec succès pour {prenom} {nom}. Dossier personnel : {cgp_path}")
    else:
        st.warning("Veuillez remplir tous les champs requis.")
