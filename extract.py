import pandas as pd

# Lire le deuxième fichier Excel
second_input_excel = "dataset_facebook-comments-scraper_2024-04-26_10-45-15-501.xlsx"  # Remplacez "autre_fichier.xlsx" par le nom de votre deuxième fichier Excel
second_df = pd.read_excel(second_input_excel)

# Extraire les données de la colonne "text" du deuxième fichier
second_text_data = second_df["text"]

# Lire le fichier existant "facebook_data.xlsx"
existing_excel = "facebook_data.xlsx"
existing_df = pd.read_excel(existing_excel)

# Concaténer les données extraites avec les données existantes
final_df = pd.concat([existing_df, pd.DataFrame({"text": second_text_data})], ignore_index=True)

# Enregistrer le DataFrame final dans le fichier "facebook_data.xlsx"
final_df.to_excel(existing_excel, index=False)

print(f"Données extraites de la colonne 'text' du deuxième fichier ajoutées à facebook_data.xlsx")
