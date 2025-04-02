param (
    [string]$projectName = "app_ia_patrimoniale_v16"
)

$zipFile = "$projectName.zip"
$githubRepo = "https://github.com/HERVELEV/patrimoine-ai.git"

Write-Host "🧹 Suppression du dossier existant..."
Remove-Item -Recurse -Force $projectName -ErrorAction SilentlyContinue

Write-Host "📦 Décompression de $zipFile..."
Expand-Archive -Path $zipFile -DestinationPath .

Set-Location $projectName

Write-Host "🌱 Initialisation Git..."
git init -b main

Write-Host "📄 Génération fichiers..."
"streamlit`npandas`nopenai" | Out-File -Encoding utf8 requirements.txt
"# IA Patrimoniale V16`nCe projet cloud Streamlit permet de lancer le déploiement GitHub automatiquement." | Out-File -Encoding utf8 README.md
".DS_Store`n__pycache__/`n*.pyc`n.env`n.vscode/`n*.log`n*.zip" | Out-File -Encoding utf8 .gitignore

git add .
git commit -m "🚀 Déploiement initial depuis Streamlit Cloud"
git remote add origin $githubRepo
git push -u origin main --force

Write-Host "✅ Projet déployé avec succès sur $githubRepo"
Pause
