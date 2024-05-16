import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Embedding
from sklearn.metrics import accuracy_score

# Charger les données à partir du fichier CSV
data = pd.read_csv("all-data.csv")

# Convertir les étiquettes de sentiment en valeurs numériques
label_encoder = LabelEncoder()
data['sentiment'] = label_encoder.fit_transform(data['sentiment'])

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(data['texte'], data['sentiment'], test_size=0.2, random_state=42)

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
    Embedding(input_dim=len(tokenizer.word_index)+1, output_dim=100, input_length=max_sequence_length),
    LSTM(64),
    Dense(1, activation='sigmoid')
])

# Compiler le modèle
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Entraîner le modèle
history = model.fit(X_train_padded, y_train, epochs=10, batch_size=32)

# Évaluer le modèle sur les données de test
loss, accuracy = model.evaluate(X_test_padded, y_test)
print("Loss:", loss)
print("Accuracy:", accuracy)

# Enregistrer les prédictions du modèle sur les données de test dans un DataFrame
y_pred = model.predict(X_test_padded)
predictions = pd.DataFrame({'True Sentiment': y_test, 'Predicted Sentiment': y_pred.flatten()})



# Calculer les statistiques pour chaque type de sentiment
sentiments = label_encoder.inverse_transform(data['sentiment'].unique())
statistics = []

for sentiment in sentiments:
    true_sentiments = predictions[predictions['True Sentiment'] == sentiment]
    total_examples = len(true_sentiments)
    if total_examples == 0:
        accuracy = None
    else:
        accuracy = accuracy_score(true_sentiments['True Sentiment'], true_sentiments['Predicted Sentiment'])
    loss = history.history['loss'][-1]  # Utiliser la dernière perte comme perte moyenne pour chaque sentiment
    statistics.append({
        'Sentiment': sentiment,
        'Total Examples': total_examples,
        'Accuracy': accuracy,
        'Loss': loss
    })

# Créer un DataFrame pandas à partir des statistiques
statistics_df = pd.DataFrame(statistics)

# Enregistrer le DataFrame dans un fichier CSV
statistics_df.to_csv('sentiment_statistics.csv', index=False)



# Créer un DataFrame pandas pour les statistiques
df_statistics = pd.DataFrame(statistics)

# Enregistrer les résultats de l'évaluation du modèle et les statistiques dans un fichier CSV
df_statistics.to_csv('sentiment_statistics.csv', index=False)
