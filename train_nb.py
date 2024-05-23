import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Charger le dataset
data = pd.read_csv('all-data.csv')

# Remplir les valeurs manquantes dans la colonne 'texte'
# data['texte'].fillna('', inplace=True)

# Vectoriser les textes
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data['texte'])

# Encoder les étiquettes de classe
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(data['sentiment'])

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraîner le modèle Naive Bayes
model = MultinomialNB()
model.fit(X_train, y_train)

# Faire des prédictions sur l'ensemble de test
y_pred = model.predict(X_test)

# Évaluer le modèle
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

classification_report_str = classification_report(y_test, y_pred, target_names=label_encoder.classes_)
print("Classification Report:")
print(classification_report_str)

conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(conf_matrix)
