import os

# Variables de configuration
api_key = "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"  # Remplace par ta clé API
secrets_file_path = "secrets.toml"
env_file_path = ".env"
gitignore_path = ".gitignore"

# 1. Créer le fichier .env pour le dépôt local
def create_env_file():
    with open(env_file_path, "w") as f:
        f.write(f"API_KEY={api_key}\n")
    print(f"Le fichier .env a été créé avec la clé API.")

# 2. Créer le fichier secrets.toml pour Streamlit Cloud
def create_secrets_file():
    secrets_content = f"""
    [secrets]
    API_KEY = "{api_key}"
    """
    with open(secrets_file_path, "w") as f:
        f.write(secrets_content)
    print(f"Le fichier {secrets_file_path} a été créé avec la clé API.")

# 3. Ajouter le fichier .env à .gitignore pour qu'il ne soit pas poussé sur GitHub
def update_gitignore():
    if os.path.exists(gitignore_path):
        with open(gitignore_path, "a") as f:
            f.write("\n.env\n")
    else:
        with open(gitignore_path, "w") as f:
            f.write(".env\n")
    print(f"Le fichier .env a été ajouté à {gitignore_path}.")

# 4. Installer les dépendances via requirements.txt
def install_dependencies():
    requirements = [
        "streamlit",
        "openai",
        "pandas",
        "fpdf",
        "twilio",
    ]
    with open("requirements.txt", "w") as f:
        f.writelines([f"{dep}\n" for dep in requirements])
    print("Le fichier requirements.txt a été mis à jour.")

# 5. Afficher des instructions de déploiement sur Streamlit Cloud
def display_deployment_instructions():
    print("\nInstructions pour déployer sur Streamlit Cloud :")
    print("1. Va sur https://share.streamlit.io/ et connecte-toi.")
    print("2. Clique sur 'Deploy an app'.")
    print("3. Dans le champ 'GitHub URL', entre l'URL de ton dépôt GitHub.")
    print("4. Dans 'Main file path', entre le nom de ton fichier principal, par exemple 'application_v16.py'.")
    print("5. Clique sur 'Deploy'.")

# Fonction principale
def main():
    print("Automatisation du processus de déploiement...")
    create_env_file()
    create_secrets_file()
    update_gitignore()
    install_dependencies()
    display_deployment_instructions()

if __name__ == "__main__":
    main()
