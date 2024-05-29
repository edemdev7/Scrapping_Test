import os
import pandas as pd

# Chemin vers le dossier contenant les fichiers Excel
dossier = "/home/edemdev/Edem/Stage/PYTHON_NPL/Scrapping_Test/LSTM"

# Initialiser une liste pour stocker les résultats
resultats = []

# Parcourir les fichiers du dossier
for fichier in os.listdir(dossier):
    if fichier.endswith(".xlsx"):
        chemin_fichier = os.path.join(dossier, fichier)
        
        # Charger le fichier Excel dans un DataFrame pandas
        df = pd.read_excel(chemin_fichier)
        
        # Compter le nombre de fois que chaque étiquette apparaît dans la colonne "sentiment"
        sentiment_counts = df['sentiment'].value_counts()
        
        # Ajouter les résultats à la liste
        resultats.append({"Fichier": fichier, "Positive": sentiment_counts.get("positive", 0),
                          "Negative": sentiment_counts.get("negative", 0),
                          "Neutral": sentiment_counts.get("neutral", 0)})

# Créer un DataFrame à partir de la liste des résultats
resultats_df = pd.DataFrame(resultats)

# Enregistrer les résultats dans un fichier CSV
resultats_df.to_csv("resultats_sentiments.csv", index=False)
