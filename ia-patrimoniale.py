import tkinter as tk
from tkinter import messagebox, filedialog
import subprocess
import os
import shutil
import zipfile

def deploy():
    zip_path = filedialog.askopenfilename(title="Sélectionne ton fichier ZIP",
                                          filetypes=[("Fichiers ZIP", "*.zip")])
    if not zip_path:
        messagebox.showwarning("Annulé", "Aucun fichier ZIP sélectionné.")
        return

    try:
        project_name = os.path.splitext(os.path.basename(zip_path))[0]
        if os.path.exists(project_name):
            shutil.rmtree(project_name)

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(".")

        subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", "lancer_deploiement.ps1", project_name], check=True)
        messagebox.showinfo("Succès", f"Déploiement de {project_name} terminé avec succès.")
    except Exception as e:
        messagebox.showerror("Erreur", f"Le script a échoué : {e}")

root = tk.Tk()
root.title("Déploiement IA Patrimoniale - Choix ZIP")
root.geometry("420x200")

label = tk.Label(root, text="Sélectionne le fichier ZIP à déployer :", font=("Arial", 12))
label.pack(pady=20)

button = tk.Button(root, text="📂 Sélectionner & 🚀 Déployer", command=deploy, font=("Arial", 14), bg="#007ACC", fg="white")
button.pack(pady=20)

root.mainloop()
