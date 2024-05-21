import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Model
from tensorflow.keras.layers import LSTM, Dense, Embedding, Input, Concatenate

# Charger les données à partir du fichier CSV
data = pd.read_csv("train_sortie.csv")

# Convertir le texte en minuscules et remplacer les valeurs NaN par des chaînes vides
data['text'].fillna('', inplace=True)
data['text'] = data['text'].apply(lambda x: x.lower())
data['selected_text'].fillna('', inplace=True)
data['selected_text'] = data['selected_text'].apply(lambda x: x.lower())

# Convertir les étiquettes de sentiment en valeurs numériques
label_encoder = LabelEncoder()
data['sentiment'] = label_encoder.fit_transform(data['sentiment'])

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(data[['text', 'selected_text']], data['sentiment'], test_size=0.2, random_state=42)

# Tokenisation et vectorisation du texte
tokenizer = Tokenizer()
tokenizer.fit_on_texts(X_train['text'].tolist() + X_train['selected_text'].tolist())

# Convertir le texte en séquences de tokens
X_train_text_sequences = tokenizer.texts_to_sequences(X_train['text'])
X_train_selected_text_sequences = tokenizer.texts_to_sequences(X_train['selected_text'])
X_test_text_sequences = tokenizer.texts_to_sequences(X_test['text'])
X_test_selected_text_sequences = tokenizer.texts_to_sequences(X_test['selected_text'])

# Rembourrage des séquences pour qu'elles aient la même longueur
max_sequence_length = max(max([len(seq) for seq in X_train_text_sequences]), max([len(seq) for seq in X_train_selected_text_sequences]))
X_train_text_padded = pad_sequences(X_train_text_sequences, maxlen=max_sequence_length, padding='post')
X_train_selected_text_padded = pad_sequences(X_train_selected_text_sequences, maxlen=max_sequence_length, padding='post')
X_test_text_padded = pad_sequences(X_test_text_sequences, maxlen=max_sequence_length, padding='post')
X_test_selected_text_padded = pad_sequences(X_test_selected_text_sequences, maxlen=max_sequence_length, padding='post')

# Convertir les étiquettes en one-hot encoding
y_train_encoded = pd.get_dummies(y_train).values
y_test_encoded = pd.get_dummies(y_test).values

# Définir l'architecture du modèle en utilisant l'API fonctionnelle de Keras
input_text = Input(shape=(max_sequence_length,), name='text_input')
input_selected_text = Input(shape=(max_sequence_length,), name='selected_text_input')

embedding_layer = Embedding(input_dim=len(tokenizer.word_index)+1, output_dim=100, input_length=max_sequence_length)
text_embedding = embedding_layer(input_text)
selected_text_embedding = embedding_layer(input_selected_text)

# LSTM layers
text_lstm = LSTM(64)(text_embedding)
selected_text_lstm = LSTM(64)(selected_text_embedding)

# Combine both LSTM layers
combined = Concatenate()([text_lstm, selected_text_lstm])
output = Dense(3, activation='softmax')(combined)  # 3 classes for sentiment

# Create the model
model = Model(inputs=[input_text, input_selected_text], outputs=output)

# Compiler le modèle
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Entraîner le modèle
history = model.fit([X_train_text_padded, X_train_selected_text_padded], y_train_encoded, epochs=10, batch_size=32, validation_data=([X_test_text_padded, X_test_selected_text_padded], y_test_encoded))

# Évaluer le modèle sur les données de test
loss, accuracy = model.evaluate([X_test_text_padded, X_test_selected_text_padded], y_test_encoded)
print("Loss:", loss)
print("Accuracy:", accuracy)

# Enregistrer les résultats de l'entraînement dans un fichier CSV
results = pd.DataFrame(history.history)
results.to_csv('training_results.csv', index=False)

# Calculer les statistiques par type de sentiment
y_pred = model.predict([X_test_text_padded, X_test_selected_text_padded])
y_pred_classes = y_pred.argmax(axis=1)
y_test_classes = y_test.values

sentiment_stats = {
    'Sentiment': [],
    'Total Examples': [],
    'Accuracy': [],
    'Loss': []
}

for sentiment in label_encoder.classes_:
    idx = label_encoder.transform([sentiment])[0]
    sentiment_mask = (y_test_classes == idx)
    sentiment_total = sentiment_mask.sum()
    sentiment_accuracy = (y_pred_classes[sentiment_mask] == idx).mean()
    sentiment_loss = -1  # Calculer la perte pour chaque sentiment si nécessaire

    sentiment_stats['Sentiment'].append(sentiment)
    sentiment_stats['Total Examples'].append(sentiment_total)
    sentiment_stats['Accuracy'].append(sentiment_accuracy)
    sentiment_stats['Loss'].append(sentiment_loss)

sentiment_stats_df = pd.DataFrame(sentiment_stats)
sentiment_stats_df.to_csv('sentiment_stats.csv', index=False)
"""
# graphe loss
plt.plot(history.history['loss'], label='loss')
plt.plot(history.history['val_loss'], label='val_loss')

plt.legend()
plt.show()

plt.savefig("Loss.jpg")

#graphe accuracy

plt.plot(history.history['accuracy'], label='acc')
plt.plot(history.history['val_accuracy'], label='val_acc')
plt.legend()
plt.show()

plt.savefig("Accuracy.jpg")
"""
# Fonction pour prédire le sentiment d'un texte donné
def predict_sentiment(text, selected_text):
    text_sequence = tokenizer.texts_to_sequences([text.lower()])
    selected_text_sequence = tokenizer.texts_to_sequences([selected_text.lower()])
    text_padded = pad_sequences(text_sequence, maxlen=max_sequence_length, padding='post')
    selected_text_padded = pad_sequences(selected_text_sequence, maxlen=max_sequence_length, padding='post')
    prediction = model.predict([text_padded, selected_text_padded])
    predicted_sentiment = label_encoder.inverse_transform(prediction.argmax(axis=1))
    return predicted_sentiment[0]

# Exemple d'utilisation
text = "the app doesn't load it's the most useless app i've ever used mtn is becoming nonsense \u0001f92c"
selected_text = "Nice"
print(" sentiment:", predict_sentiment(text, selected_text))
