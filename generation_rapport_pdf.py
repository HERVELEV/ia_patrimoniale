
import streamlit as st
from fpdf import FPDF

# Fonction pour calculer le rendement estimé d'un investissement
def calculate_investment_return(principal, years, annual_rate):
    return principal * (1 + annual_rate) ** years

# Fonction pour calculer l'impact fiscal basé sur le produit choisi
def calculate_fiscal_impact(product_choice, investment_amount, years, rate):
    if product_choice == "Assurance Vie":
        annual_return = calculate_investment_return(investment_amount, years, rate)
        taxable_gain = annual_return - investment_amount
        tax = taxable_gain * 0.128  # Impôt sur les gains
        return tax, annual_return

    elif product_choice == "SCPI":
        annual_return = calculate_investment_return(investment_amount, years, rate)
        taxable_gain = annual_return - investment_amount
        tax = taxable_gain * 0.30  # Impôt sur les gains
        return tax, annual_return

    elif product_choice == "Fonds en Actions":
        annual_return = calculate_investment_return(investment_amount, years, rate)
        taxable_gain = annual_return - investment_amount
        tax = taxable_gain * 0.172  # Impôt sur les dividendes
        return tax, annual_return

    elif product_choice == "Immobilier (LMNP)":
        annual_return = calculate_investment_return(investment_amount, years, rate)
        taxable_gain = annual_return - investment_amount
        tax = taxable_gain * 0.25  # Abattement fiscal appliqué à 30% des revenus
        return tax, annual_return

    else:
        return 0, 0

# Fonction pour générer un rapport PDF
def generate_pdf_report(product_choice, investment_amount, investment_years, rate, tax, final_value):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.set_font('Arial', 'B', 16)
    pdf.cell(200, 10, 'Rapport de Simulation d'Investissement', ln=True, align='C')

    pdf.set_font('Arial', '', 12)
    pdf.ln(10)
    pdf.cell(200, 10, f"Produit choisi : {product_choice}", ln=True)
    pdf.cell(200, 10, f"Montant investi : {investment_amount} €", ln=True)
    pdf.cell(200, 10, f"Durée de l'investissement : {investment_years} ans", ln=True)
    pdf.cell(200, 10, f"Taux de rendement estimé : {rate * 100} %", ln=True)
    pdf.cell(200, 10, f"Valeur finale estimée (avant impôts) : {final_value:.2f} €", ln=True)
    pdf.cell(200, 10, f"Impact fiscal estimé (impôt sur les gains) : {tax:.2f} €", ln=True)

    file_path = f"/mnt/data/simulation_{product_choice.replace(' ', '_')}_{investment_years}_ans.pdf"
    pdf.output(file_path)

    return file_path

# Interface Streamlit pour afficher le rapport PDF
st.title("Génération du Rapport PDF d'Investissement")

product_choice = st.selectbox("Sélectionnez un produit d'investissement", ["Assurance Vie", "SCPI", "Fonds en Actions", "Immobilier (LMNP)"])
investment_amount = st.number_input("Montant à investir (€)", min_value=1000)
investment_years = st.slider("Durée de l'investissement (années)", min_value=1, max_value=30, step=1)

if product_choice == "Assurance Vie":
    rate = 0.02
elif product_choice == "SCPI":
    rate = 0.05
elif product_choice == "Fonds en Actions":
    rate = 0.07
elif product_choice == "Immobilier (LMNP)":
    rate = 0.04

if st.button("Générer le rapport PDF"):
    tax, final_value = calculate_fiscal_impact(product_choice, investment_amount, investment_years, rate)
    report_path = generate_pdf_report(product_choice, investment_amount, investment_years, rate, tax, final_value)
    
    st.write(f"**Produit choisi :** {product_choice}")
    st.write(f"**Montant investi :** {investment_amount} €")
    st.write(f"**Durée de l'investissement :** {investment_years} ans")
    st.write(f"**Taux de rendement estimé :** {rate * 100} %")
    st.write(f"**Valeur finale estimée (avant impôts) :** {final_value:.2f} €")
    st.write(f"**Impact fiscal estimé (impôt sur les gains) :** {tax:.2f} €")
    
    st.write(f"**Votre rapport PDF est prêt !**")
    st.download_button(
        label="Télécharger le rapport PDF",
        data=open(report_path, "rb").read(),
        file_name=report_path.split("/")[-1],
        mime="application/pdf"
    )
