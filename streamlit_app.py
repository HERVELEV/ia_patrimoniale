
import streamlit as st

st.set_page_config(page_title="IA Patrimoniale", layout="wide")

# Sidebar
st.sidebar.title("Menu IA Patrimoniale")
menu = st.sidebar.radio("Navigation", [
    "🏠 Accueil",
    "🧾 Collecte Client",
    "📈 Simulation",
    "📄 Documents",
    "⚙️ Suivi & Audit"
])

# Accueil
if menu == "🏠 Accueil":
    st.title("Bienvenue dans votre Assistant IA Patrimoniale")
    st.markdown("""
    Cette application vous permet d'automatiser l'ensemble du parcours réglementaire
    et patrimonial de vos clients grâce à l'intelligence artificielle.
    


    **Modules inclus à venir :**
    - Collecte client (RGPD, KYC)
    - Simulation patrimoniale
    - Génération automatique de documents réglementaires (DDA, LM, etc.)
    - Recommandation IA & Analyse émotionnelle
    - Export vers Wizio / Signature électronique
    """)

# Collecte Client
elif menu == "🧾 Collecte Client":
    st.header("Formulaire de collecte client - Étape 1")

    with st.form("formulaire_client"):
        nom = st.text_input("Nom")
        prenom = st.text_input("Prénom")
        email = st.text_input("Adresse Email")
        telephone = st.text_input("Téléphone")
        consentement = st.checkbox("✅ J'accepte le traitement de mes données personnelles (RGPD)")

        submitted = st.form_submit_button("Continuer")
        if submitted:
            if nom and prenom and email and consentement:
                st.success("Données enregistrées. Étape suivante : Profil de risque.")
            else:
                st.error("Merci de remplir tous les champs obligatoires et cocher le consentement.")

# Simulation (placeholder)
elif menu == "📈 Simulation":
    st.header("📊 Simulation patrimoniale (à venir)")
    st.info("Module en développement – Phase 3.")

# Documents (placeholder)
elif menu == "📄 Documents":
    st.header("📄 Génération des documents réglementaires (à venir)")
    st.info("Module en développement – Phase 4 & 6.")

# Audit
elif menu == "⚙️ Suivi & Audit":
    st.header("📋 Journal des interactions (à venir)")
    st.info("Module audit trail et mémoire IA – Phase 7.")
