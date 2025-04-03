
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Dashboard CGP", layout="wide")
st.title("Tableau de bord - Conseiller en Gestion de Patrimoine")

# Chargement des données
client_data_path = "data/client_data.csv"
dda_data_path = "data/dda_data.csv"
lm_path = "generated_pdfs"
signatures_path = "data/signature_tracking.csv"

nb_clients = 0
nb_lm = 0
nb_dda = 0
nb_signatures = 0

if os.path.exists(client_data_path):
    df_clients = pd.read_csv(client_data_path)
    nb_clients = len(df_clients)

if os.path.exists(lm_path):
    nb_lm = len([f for f in os.listdir(lm_path) if f.endswith(".pdf")])

if os.path.exists(dda_data_path):
    df_dda = pd.read_csv(dda_data_path)
    nb_dda = len(df_dda)

if os.path.exists(signatures_path):
    df_signatures = pd.read_csv(signatures_path)
    nb_signatures = len(df_signatures)

# Affichage des KPIs
st.subheader("Vue d'ensemble")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Clients enregistrés", nb_clients)
col2.metric("Lettres de mission", nb_lm)
col3.metric("Rapports DDA générés", nb_dda)
col4.metric("Signatures suivies", nb_signatures)

# Tableau clients
st.markdown("### Liste des clients")
if nb_clients > 0:
    st.dataframe(df_clients)
else:
    st.info("Aucun client enregistré actuellement.")
