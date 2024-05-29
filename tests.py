import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Embedding
from tensorflow.keras.losses import CategoricalCrossentropy
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.sequence import pad_sequences
from googletrans import Translator

# Charger les données à partir du fichier CSV
data = pd.read_csv("train.csv", encoding='latin-1')

# Remplacer les valeurs manquantes par une chaîne vide
data['text'].fillna('', inplace=True)
# Prétraitement des emojis
#demoji.download_codes()  # Télécharger le répertoire d'emojis
#data['text'] = data['text'].apply(lambda x: demoji.replace(x, ""))


# Convertir les étiquettes de sentiment en valeurs numériques
label_encoder = LabelEncoder()
data['sentiment'] = label_encoder.fit_transform(data['sentiment'])

# Convertir les étiquettes en one-hot encoding
y = to_categorical(data['sentiment'])

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(data['text'], y, test_size=0.2, random_state=42)

# Tokenisation et vectorisation du texte
tokenizer = Tokenizer()
tokenizer.fit_on_texts(X_train)
X_train_sequences = tokenizer.texts_to_sequences(X_train)
X_test_sequences = tokenizer.texts_to_sequences(X_test)

# Rembourrage des séquences pour qu'elles aient la même longueur
max_sequence_length = max([len(seq) for seq in X_train_sequences])
X_train_padded = pad_sequences(X_train_sequences, maxlen=max_sequence_length, padding='post')
X_test_padded = pad_sequences(X_test_sequences, maxlen=max_sequence_length, padding='post')

# Créer le modèle LSTM
model = Sequential([
    Embedding(input_dim=len(tokenizer.word_index)+1, output_dim=64),
    LSTM(128, return_sequences=False),
    Dense(3, activation='softmax')
])

# Compiler le modèle
model.compile(optimizer='adam', loss=CategoricalCrossentropy(), metrics=['accuracy'])

# Entraîner le modèle
history = model.fit(X_train_padded, y_train, validation_split=0.2, epochs=100, batch_size=32)

# Évaluer le modèle
loss, accuracy = model.evaluate(X_test_padded, y_test)
print(f"Test Loss: {loss}")
print(f"Test Accuracy: {accuracy}")





def predict_sentiment(model, tokenizer, excel_file, output_file):
    # Charger le fichier Excel
    data = pd.read_excel(excel_file)
    
    # Prétraiter les données de texte nettoyé
    X_sequences = []
    for text in data['texte_nettoye']:
        if isinstance(text, float):  # Vérifier si la valeur est flottante
            X_sequences.append('')   # Remplacer les valeurs flottantes par des chaînes vides
        else:
            X_sequences.append(text)
    
    X_padded = pad_sequences(tokenizer.texts_to_sequences(X_sequences), maxlen=max_sequence_length, padding='post')
    
    # Prédire les sentiments pour chaque texte
    predictions = model.predict(X_padded)
    
    # Récupérer les indices des classes prédites
    predicted_classes = predictions.argmax(axis=1)
    
    # Convertir les indices en labels de sentiment
    predicted_sentiments = label_encoder.inverse_transform(predicted_classes)
    
    # Ajouter une nouvelle colonne "sentiment" au DataFrame Excel avec les prédictions
    data['sentiment'] = predicted_sentiments
    
    # Sauvegarder le DataFrame mis à jour dans un nouveau fichier Excel
    data.to_excel(output_file, index=False)
    
    print("Prédictions de sentiment ajoutées au fichier Excel avec succès.")


# Utilisation de la fonction pour prédire les sentiments dans un fichier Excel
predict_sentiment(model, tokenizer, "/home/edemdev/Edem/Stage/PYTHON_NPL/Scrapping_Test/Dataset_nettoye/celtisss.xlsx", "LSTM/celtiis_LSTM_sortie.xlsx")
