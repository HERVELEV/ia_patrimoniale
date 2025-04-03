
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Catalogue Produits", layout="centered")
st.title("Catalogue des Produits Partenaires")

csv_path = "produits_partenaire.csv"

# Chargement du fichier
try:
    df = pd.read_csv(csv_path)
    st.success(f"{len(df)} produits chargés.")
    
    # Filtres
    partenaires = st.multiselect("Filtrer par partenaire", options=sorted(df["Partenaire"].unique()), default=sorted(df["Partenaire"].unique()))
    types = st.multiselect("Filtrer par type de produit", options=sorted(df["Type"].unique()), default=sorted(df["Type"].unique()))
    profils = st.multiselect("Filtrer par profil cible", options=sorted(df["Profil cible"].unique()), default=sorted(df["Profil cible"].unique()))

    # Application des filtres
    df_filtré = df[
        (df["Partenaire"].isin(partenaires)) &
        (df["Type"].isin(types)) &
        (df["Profil cible"].isin(profils))
    ]

    st.dataframe(df_filtré)

    for i, row in df_filtré.iterrows():
        st.markdown(f"### {row['Nom du produit']}")
        st.write(f"**Partenaire :** {row['Partenaire']}")
        st.write(f"**Type :** {row['Type']} | **Profil cible :** {row['Profil cible']}")
        st.write(f"**Durée :** {row['Durée']} | **Rendement :** {row['Rendement cible']}")
        st.write(f"**Commentaire :** {row['Commentaire']}")
        st.markdown(f"[Fiche produit]({row['Lien DIC/Fiche']})", unsafe_allow_html=True)
        st.markdown("---")

except FileNotFoundError:
    st.error("Fichier produits_partenaire.csv introuvable. Merci de le déposer dans le dossier de l’application.")
