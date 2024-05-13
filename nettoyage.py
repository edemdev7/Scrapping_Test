import pandas as pd
import re
from bs4 import BeautifulSoup
import emoji
from textblob import TextBlob


def clean_text(text):
    if pd.isna(text):  # Vérifier si le texte est NaN
        return ""  # Retourner une chaîne vide pour les valeurs NaN
    else:
        # Supprimer les balises HTML
        text = BeautifulSoup(text, "html.parser").get_text()
        
        # Convertir les émojis en leur équivalent en code ASCII
        text = emoji.demojize(text)
        
        # Convertir les émojis en leur équivalent en code ASCII HTML
        text = re.sub(r":\w+:", lambda m: emoji.emojize(m.group(0)).encode('unicode-escape').decode('utf-8'), text)

        # Ajouter un espace entre les émojis et les autres caractères
        text = re.sub(r'(\S)(?=:)', r'\1 ', text)
        text = re.sub(r'(?<=:)(\S)', r' \1', text)
        
        # Supprimer les caractères spéciaux spécifiques
        text = re.sub(r"[#@/|]", " ", str(text))
        
        # Convertir le texte en minuscules
        text = text.lower()

        # Correction orthographique
        #text_blob = TextBlob(text)
        #text = str(text_blob.correct())
        
        return text

# Charger le fichier Excel
df = pd.read_excel("/home/edemdev/Edem/Stage/PYTHON_NPL/Scrapping_Test/Datasets/Mtn_app.xlsx")

# Appliquer la fonction de nettoyage à la colonne de texte
df["texte_nettoye"] = df["text"].apply(clean_text)

# Afficher les premières lignes du dataframe avec la colonne nettoyée
print(df.head())


# Enregistrer le DataFrame avec la colonne nettoyée dans un fichier Excel
df.to_excel("Dataset_nettoye/Mtn_app.xlsx", index=False)
