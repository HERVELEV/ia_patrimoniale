
import streamlit as st
import pandas as pd
import openai

st.set_page_config(page_title="Recommandation IA Patrimoniale", layout="centered")
st.title("Recommandations IA – Stratégie d'investissement personnalisée")

openai.api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else "sk-..."

# Chargement des données clients
file_path = "data/client_data.csv"
if not os.path.exists(file_path):
    st.warning("Aucune donnée client disponible.")
else:
    df = pd.read_csv(file_path)
    selected_client = st.selectbox("Choisir un client", df["Nom"].unique())

    client_data = df[df["Nom"] == selected_client].iloc[0]
    st.write("Données du client :", client_data)

    if st.button("Générer la recommandation IA"):
        prompt = f"""
Tu es un conseiller en gestion de patrimoine agréé CIF-AMF.
Voici les données d’un client :

Nom : {client_data["Nom"]}
Âge : {client_data["Âge"]}
Revenu annuel : {client_data["Revenu"]}
Patrimoine total : {client_data["Patrimoine"]}
Objectif : {client_data["Objectif"]}
Profil de risque : {client_data["Profil"]}

Propose une stratégie patrimoniale personnalisée avec :
- Produits adaptés au profil (fonds euros, SCPI, structuré, assurance vie, etc.)
- Justification pédagogique
- Horizon conseillé
- Répartition indicative
- Approche fiscale

Réponds de manière claire et professionnelle.
        """

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=800
        )

        strategy = response.choices[0].message.content.strip()
        st.subheader("Recommandation personnalisée :")
        st.write(strategy)
