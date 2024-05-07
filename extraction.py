import pandas as pd

# Lire le fichier Excel
input_excel = "mtn_south_africa.xlsx"  # Remplacez "votre_fichier.xlsx" par le nom de votre fichier Excel
df = pd.read_excel(input_excel)

# Extraire les données de la colonne "text"
text_data = df["content"]

# Créer un nouveau DataFrame avec les données extraites
new_df = pd.DataFrame({"content": text_data})

# Enregistrer le nouveau DataFrame dans un fichier Excel
output_excel = "moov_south_app.xlsx"
new_df.to_excel(output_excel, index=False)

print(f"Données extraites de la colonne 'text' et enregistrées dans le fichier Excel : {output_excel}")
