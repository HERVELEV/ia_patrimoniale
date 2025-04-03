
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Fonction pour calculer le rendement estimé d'un investissement
def calculate_investment_return(principal, years, annual_rate):
    # Formule d'intérêt composé : A = P(1 + r/n)^(nt)
    return principal * (1 + annual_rate) ** years

# Fonction pour afficher un graphique de simulation de rendement
def plot_investment_return(principal, years, rate, product_name):
    years_range = np.arange(1, years + 1)
    values = [calculate_investment_return(principal, year, rate) for year in years_range]
    
    plt.figure(figsize=(10, 6))
    plt.plot(years_range, values, label=f'Rendement de {product_name}', color='blue')
    plt.title(f"Simulation de rendement pour {product_name}")
    plt.xlabel('Années')
    plt.ylabel('Valeur estimée de l'investissement (€)')
    plt.grid(True)
    plt.legend()
    st.pyplot(plt)

# Interface utilisateur Streamlit pour la simulation d'investissement
st.title("Simulation d'Investissement")

# Collecte des données via formulaire
product_choice = st.selectbox("Sélectionnez un produit d'investissement", ["Assurance Vie", "SCPI", "Fonds en Actions", "Immobilier (LMNP)"])

# Entrée des données utilisateur
investment_amount = st.number_input("Montant à investir (€)", min_value=1000)
investment_years = st.slider("Durée de l'investissement (années)", min_value=1, max_value=30, step=1)

# Taux de rendement selon le produit sélectionné (hypothèses de rendement annuel)
if product_choice == "Assurance Vie":
    rate = 0.02  # Rendement de 2% pour l'assurance vie
elif product_choice == "SCPI":
    rate = 0.05  # Rendement de 5% pour les SCPI
elif product_choice == "Fonds en Actions":
    rate = 0.07  # Rendement de 7% pour les actions
elif product_choice == "Immobilier (LMNP)":
    rate = 0.04  # Rendement de 4% pour l'immobilier

# Calcul et affichage des résultats
if st.button("Lancer la simulation"):
    st.write(f"**Produit choisi :** {product_choice}")
    st.write(f"**Montant investi :** {investment_amount} €")
    st.write(f"**Durée de l'investissement :** {investment_years} ans")
    st.write(f"**Taux de rendement estimé :** {rate * 100} %")

    # Calcul du rendement total à la fin de la période
    final_value = calculate_investment_return(investment_amount, investment_years, rate)
    st.write(f"**Valeur finale estimée :** {final_value:.2f} €")

    # Affichage du graphique de la simulation de rendement
    plot_investment_return(investment_amount, investment_years, rate, product_choice)

# Collecte d'une question supplémentaire à poser à l'IA
user_question = st.text_input("Vous avez des questions pour l'IA ?", "Quels sont les risques de ce produit ?")
if user_question:
    st.write(f"**Réponse de l'IA :** En fonction de votre profil, voici les principaux risques associés à ce produit : ...")
