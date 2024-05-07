import os
import pandas as pd

# Chemin du dossier contenant les fichiers Excel
input_folder = "Old_data"

# Créer un dossier pour stocker les fichiers avec uniquement la colonne "content"
output_folder = os.path.join(input_folder, "Content")
os.makedirs(output_folder, exist_ok=True)

# Parcourir tous les fichiers dans le dossier
for filename in os.listdir(input_folder):
    if filename.endswith(".xlsx"):
        # Lire le fichier Excel
        filepath = os.path.join(input_folder, filename)
        df = pd.read_excel(filepath)
        
        # Extraire uniquement la colonne "content"
        content_column = df["content"]
        
        # Créer un nouveau DataFrame avec uniquement la colonne "content"
        content_df = pd.DataFrame({"content": content_column})
        
        # Chemin pour le nouveau fichier Excel avec uniquement la colonne "content"
        output_filepath = os.path.join(output_folder, f"Content_{filename}")
        
        # Écrire le DataFrame dans un nouveau fichier Excel
        content_df.to_excel(output_filepath, index=False)

print("Extraction des éléments de la colonne 'content' terminée.")
