import pandas as pd

# Lire le fichier Excel
input_excel = "dataset_facebook-comments-scraper_2024-04-25_11-55-47-706.xlsx"  # Remplacez "votre_fichier.xlsx" par le nom de votre fichier Excel
df = pd.read_excel(input_excel)

# Extraire les données de la colonne "text"
text_data = df["text"]

# Créer un nouveau DataFrame avec les données extraites
new_df = pd.DataFrame({"text": text_data})

# Enregistrer le nouveau DataFrame dans un fichier Excel
output_excel = "facebook_data.xlsx"
new_df.to_excel(output_excel, index=False)

print(f"Données extraites de la colonne 'text' et enregistrées dans le fichier Excel : {output_excel}")
