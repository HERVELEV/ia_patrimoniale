
import pandas as pd
from fpdf import FPDF
import os

def generate_pdf(nom_client, objectif):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Lettre de Mission – {nom_client}", ln=True, align="C")
    pdf.ln(10)
    pdf.multi_cell(0, 10, f"Objet de la mission : {objectif}\n\nEn ma qualité de Conseiller en Investissements Financiers, j’interviens dans le cadre d’une mission de conseil conforme aux exigences de l’AMF.\n\nJe m’engage à fournir un conseil adapté à la situation patrimoniale et aux objectifs exprimés.")
    if not os.path.exists("generated_pdfs"):
        os.makedirs("generated_pdfs")
    filename = f"generated_pdfs/lettre_mission_{nom_client.replace(' ', '_')}.pdf"
    pdf.output(filename)
    return filename

def generate_documents_for_clients():
    df = pd.read_csv("data/client_data.csv")
    for _, row in df.iterrows():
        client_name = row["Nom"]
        objectif = row["Objectif"]
        path = generate_pdf(client_name, objectif)
        print(f"Lettre générée : {path}")

if __name__ == "__main__":
    generate_documents_for_clients()
