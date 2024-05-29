from googletrans import Translator
import pandas as pd
import re
from bs4 import BeautifulSoup
import emoji
from textblob import TextBlob

# Créer une instance du traducteur
translator = Translator()

def clean_text(text):
    if pd.isna(text):  # Vérifier si le texte est NaN
        return ""  # Retourner une chaîne vide pour les valeurs NaN
    else:
        # Supprimer les balises HTML
        text = BeautifulSoup(text, "html.parser").get_text()
        
        # Traduire le texte en anglais s'il n'est pas déjà en anglais
        try:
            translated_text = translator.translate(text, src='fr', dest='en').text
        except Exception as e:
            print(f"Error translating text: {e}")
            translated_text = text  # Retourner le texte original en cas d'erreur
            
        # Convertir les émojis en leur équivalent en code ASCII
        translated_text = emoji.demojize(translated_text)
        
        # Ajouter un espace entre les émojis et les autres caractères
        translated_text = re.sub(r'(\S)(?=:)', r'\1 ', translated_text)
        translated_text = re.sub(r'(?<=:)(\S)', r' \1', translated_text)
        
        # Supprimer les caractères spéciaux spécifiques
        translated_text = re.sub(r"[#@/|]", " ", translated_text)
        
        # Convertir le texte en minuscules
        translated_text = translated_text.lower()

        # Correction orthographique
        #text_blob = TextBlob(translated_text)
        #translated_text = str(text_blob.correct())
        
        return translated_text


# Charger le fichier Excel
df = pd.read_excel("/home/edemdev/Edem/Stage/PYTHON_NPL/Scrapping_Test/Dataset_nettoye/facebook_mtn_internet.xlsx")

# Appliquer la fonction de nettoyage à la colonne de texte
df["texte_nettoye"] = df["text"].apply(clean_text)

# Afficher les premières lignes du dataframe avec la colonne nettoyée
print(df.head())


# Enregistrer le DataFrame avec la colonne nettoyée dans un fichier Excel
df.to_excel("Dataset_nettoye/nettoye_mtn_internet.xlsx", index=False)
