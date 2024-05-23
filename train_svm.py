import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score

# Charger les données en spécifiant l'encodage latin-1
data = pd.read_csv("train.csv", encoding='latin-1')


# Afficher les premières lignes pour vérifier le chargement
#print(data.head())

# Remplacer les valeurs manquantes par une chaîne vide
data['text'].fillna('', inplace=True)
#data['sentiment'].fillna('', inplace=True)
# Encoder les étiquettes de sentiment en valeurs numériques
label_encoder = LabelEncoder()
data['sentiment'] = label_encoder.fit_transform(data['sentiment'])

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(data['text'], data['sentiment'], test_size=0.2, random_state=42)

# Vectoriser les textes en utilisant TF-IDF
vectorizer = TfidfVectorizer(max_features=5000)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Initialiser le modèle SVM avec un noyau linéaire
svm_model = SVC(kernel='linear', C=1.0, random_state=42)

# Entraîner le modèle
svm_model.fit(X_train_tfidf, y_train)

# Prédire les étiquettes pour les données de test
y_pred = svm_model.predict(X_test_tfidf)

# Évaluer le modèle
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=label_encoder.classes_)

print(f"Accuracy: {accuracy}")
print(f"Classification Report:\n{report}")

def predict_sentiment_svm(model, vectorizer, excel_file, output_file):
    # Charger le fichier Excel
    data = pd.read_excel(excel_file)
    
     # Remplacer les valeurs manquantes par une chaîne vide
    data['texte_nettoye'].fillna('', inplace=True)
    
    # Prétraiter les données de texte nettoyé
    X_tfidf = vectorizer.transform(data['texte_nettoye'])
    
    # Prédire les sentiments pour chaque texte
    y_pred = model.predict(X_tfidf)
    
    # Convertir les étiquettes prédites en noms de classe
    predicted_sentiments = label_encoder.inverse_transform(y_pred)
    
    # Ajouter une nouvelle colonne "sentiment" au DataFrame Excel avec les prédictions
    data['sentiment'] = predicted_sentiments
    
    # Sauvegarder le DataFrame mis à jour dans un nouveau fichier Excel
    data.to_excel(output_file, index=False)
    
    print("Prédictions de sentiment ajoutées au fichier Excel avec succès.")

# Utilisation de la fonction pour prédire les sentiments dans un fichier Excel
predict_sentiment_svm(svm_model, vectorizer, "/home/edemdev/Edem/Stage/PYTHON_NPL/Scrapping_Test/Dataset_nettoye/Mtn_app.xlsx", "fichier_sortie_svm.xlsx")
