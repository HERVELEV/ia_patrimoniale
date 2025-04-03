
import streamlit as st
import os
import chromadb
from chromadb.config import Settings
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

st.set_page_config(page_title="Mémoire IA - ChromaDB", layout="centered")
st.title("Mémoire intelligente IA - Historique conversationnel")

st.markdown("Ce module permet de stocker les échanges client-IA dans une base vectorielle ChromaDB pour les retrouver plus tard.")

client = st.text_input("Nom du client")

question = st.text_area("Question posée au client")
reponse = st.text_area("Réponse fournie par l'IA")

if st.button("Ajouter à la mémoire IA"):
    if client and question and reponse:
        persist_dir = "vector_db"
        if not os.path.exists(persist_dir):
            os.makedirs(persist_dir)

        # Configuration de ChromaDB
        chroma_client = chromadb.Client(Settings(
            chroma_db_impl="duckdb+parquet",
            persist_directory=persist_dir
        ))

        embedding_function = OpenAIEmbeddingFunction(api_key=os.getenv("OPENAI_API_KEY"))
        collection = chroma_client.get_or_create_collection(name=client, embedding_function=embedding_function)

        # Ajout du document
        doc_id = f"{client}_{len(collection.get()['ids']) + 1}"
        collection.add(
            documents=[f"Q: {question} \nR: {reponse}"],
            ids=[doc_id],
            metadatas=[{"client": client}]
        )

        chroma_client.persist()
        st.success("Échange ajouté à la mémoire vectorielle.")
    else:
        st.warning("Veuillez remplir tous les champs.")
