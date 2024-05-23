import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score

# Charger les données
data = pd.read_csv("all-data.csv")

# Afficher les premières lignes pour vérifier le chargement
#print(data.head())

# Remplacer les valeurs manquantes par une chaîne vide
#data['texte'].fillna('', inplace=True)

# Encoder les étiquettes de sentiment en valeurs numériques
label_encoder = LabelEncoder()
data['sentiment'] = label_encoder.fit_transform(data['sentiment'])

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(data['texte'], data['sentiment'], test_size=0.2, random_state=42)

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

