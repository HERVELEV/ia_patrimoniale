
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Fonction pour calculer le rendement estimé d'un investissement
def calculate_investment_return(principal, years, annual_rate):
    # Formule d'intérêt composé : A = P(1 + r/n)^(nt)
    return principal * (1 + annual_rate) ** years

# Fonction pour calculer l'impact fiscal basé sur le produit choisi
def calculate_fiscal_impact(product_choice, investment_amount, years, rate):
    if product_choice == "Assurance Vie":
        # Exemple : Rendement annuel de 2% avec une imposition de 12.8% sur les gains
        annual_return = calculate_investment_return(investment_amount, years, rate)
        taxable_gain = annual_return - investment_amount
        tax = taxable_gain * 0.128  # Impôt sur les gains
        return tax, annual_return

    elif product_choice == "SCPI":
        # Exemple : Rendement de 5% avec un impôt sur les plus-values de 30%
        annual_return = calculate_investment_return(investment_amount, years, rate)
        taxable_gain = annual_return - investment_amount
        tax = taxable_gain * 0.30  # Impôt sur les gains
        return tax, annual_return

    elif product_choice == "Fonds en Actions":
        # Exemple : Rendement de 7% avec un impôt sur les dividendes de 17.2%
        annual_return = calculate_investment_return(investment_amount, years, rate)
        taxable_gain = annual_return - investment_amount
        tax = taxable_gain * 0.172  # Impôt sur les dividendes
        return tax, annual_return

    elif product_choice == "Immobilier (LMNP)":
        # Exemple : Rendement de 4% avec un abattement fiscal de 30% pour les revenus locatifs
        annual_return = calculate_investment_return(investment_amount, years, rate)
        taxable_gain = annual_return - investment_amount
        tax = taxable_gain * 0.25  # Abattement fiscal appliqué à 30% des revenus
        return tax, annual_return

    else:
        return 0, 0

# Interface Streamlit pour afficher les résultats
st.title("Simulation d'Impact Fiscal d'Investissement")

# Collecte des données via formulaire
product_choice = st.selectbox("Sélectionnez un produit d'investissement", ["Assurance Vie", "SCPI", "Fonds en Actions", "Immobilier (LMNP)"])

investment_amount = st.number_input("Montant à investir (€)", min_value=1000)
investment_years = st.slider("Durée de l'investissement (années)", min_value=1, max_value=30, step=1)

# Taux de rendement selon le produit sélectionné
if product_choice == "Assurance Vie":
    rate = 0.02  # Rendement de 2% pour l'assurance vie
elif product_choice == "SCPI":
    rate = 0.05  # Rendement de 5% pour les SCPI
elif product_choice == "Fonds en Actions":
    rate = 0.07  # Rendement de 7% pour les actions
elif product_choice == "Immobilier (LMNP)":
    rate = 0.04  # Rendement de 4% pour l'immobilier

# Calcul de l'impact fiscal et de la valeur totale
if st.button("Lancer la simulation fiscale"):
    # Calcul du rendement estimé et de l'impact fiscal
    tax, final_value = calculate_fiscal_impact(product_choice, investment_amount, investment_years, rate)
    
    st.write(f"**Produit choisi :** {product_choice}")
    st.write(f"**Montant investi :** {investment_amount} €")
    st.write(f"**Durée de l'investissement :** {investment_years} ans")
    st.write(f"**Taux de rendement estimé :** {rate * 100} %")
    st.write(f"**Valeur finale estimée (avant impôts) :** {final_value:.2f} €")
    st.write(f"**Impact fiscal estimé (impôt sur les gains) :** {tax:.2f} €")
