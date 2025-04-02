
import os
import shutil
import subprocess
from pathlib import Path

def deploy_project(project_name, zip_file):
    # Nettoyage préalable
    if os.path.exists(project_name):
        shutil.rmtree(project_name)

    # Décompression
    shutil.unpack_archive(zip_file, project_name)

    # Initialisation Git
    os.chdir(project_name)
    subprocess.run(["git", "init", "-b", "main"], check=True)

    # Configurer identité Git
    subprocess.run(["git", "config", "user.email", "herve.levy61@gmail.com"], check=True)
    subprocess.run(["git", "config", "user.name", "Hervé Lévy"], check=True)

    # Fichiers à générer
    Path("requirements.txt").write_text("streamlit\npandas\nopenai")
    Path("README.md").write_text("# IA Patrimoniale V16\nProjet déployé depuis Streamlit Cloud.")
    Path(".gitignore").write_text(".DS_Store\n__pycache__/\n*.pyc\n.env\n.vscode/\n*.log\n*.zip")

    # Commit Git
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "🚀 Déploiement initial depuis Streamlit Cloud"], check=True)

    # ✅ URL avec token à compléter par toi-même
    github_repo = "https://ghp_IxKEQ87[...]@github.com/HERVELEV/patrimoine-ai.git"

    # Push GitHub
    subprocess.run(["git", "remote", "add", "origin", github_repo], check=True)
    subprocess.run(["git", "push", "-u", "origin", "main", "--force"], check=True)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python deploy.py <project_name> <zip_file>")
    else:
        deploy_project(sys.argv[1], sys.argv[2])
