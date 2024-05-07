import os
import pandas as pd

# Chemin du dossier contenant les fichiers Excel
folder_path = "/home/edemdev/Edem/Stage/PYTHON_NPL/Scrapping_Test/MTN"

# Liste pour stocker les données extraites de chaque fichier
data_list = []

# Parcourir tous les fichiers dans le dossier
for file_name in os.listdir(folder_path):
    if file_name.endswith(".xlsx"):  # Vérifier si le fichier est un fichier Excel
        file_path = os.path.join(folder_path, file_name)
        # Lire le fichier Excel et extraire la colonne 'text'
        df = pd.read_excel(file_path)
        if 'content' in df.columns:
            data_list.extend(df['content'].tolist())

# Créer un DataFrame à partir des données extraites
facebook_data = pd.DataFrame({'content': data_list})

# Enregistrer les données dans un nouveau fichier Excel
output_file = "Mtn_app.xlsx"
facebook_data.to_excel(output_file, index=False)

print(f"Données extraites enregistrées dans le fichier Excel : {output_file}")
