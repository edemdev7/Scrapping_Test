import pandas as pd
from google_play_scraper import app

# Obtenir les données de l'application
result = app(
    'com.nianticlabs.pokemongo',
    lang='en', # langue par défaut 'en'
    country='us' # pays par défaut 'us'
)

# Créer un DataFrame à partir des données
df = pd.DataFrame([result])

# Enregistrer le DataFrame dans un fichier Excel
excel_file = "app_data.xlsx"
df.to_excel(excel_file, index=False)

# Afficher les données dans la console
print("Données de l'application :")
print(df)

print(f"Données de l'application enregistrées dans le fichier Excel : {excel_file}")
