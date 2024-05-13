import pandas as pd
from sklearn.model_selection import train_test_split
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import LSTM, Embedding, Dense

# Charger les données à partir du fichier CSV
data = pd.read_csv("all-data.csv")

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(data['texte'], data['sentiment'], test_size=0.2, random_state=42)

# Convertir les textes en séquences numériques
tokenizer = Tokenizer()
tokenizer.fit_on_texts(X_train)
X_train_seq = tokenizer.texts_to_sequences(X_train)
X_test_seq = tokenizer.texts_to_sequences(X_test)

# Remplir les séquences pour qu'elles aient la même longueur
max_sequence_length = 100  # Choisissez la longueur maximale souhaitée pour vos séquences
X_train_pad = pad_sequences(X_train_seq, maxlen=max_sequence_length)
X_test_pad = pad_sequences(X_test_seq, maxlen=max_sequence_length)

# Créer un modèle LSTM
model = Sequential()
model.add(Embedding(input_dim=len(tokenizer.word_index)+1, output_dim=100, input_length=max_sequence_length))
model.add(LSTM(units=64))
model.add(Dense(units=1, activation='sigmoid'))

# Compiler le modèle
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Entraîner le modèle
model.fit(X_train_pad, y_train, epochs=10, batch_size=32, validation_data=(X_test_pad, y_test))

# Évaluer le modèle sur les données de test
loss, accuracy = model.evaluate(X_test_pad, y_test)
print("Loss:", loss)
print("Accuracy:", accuracy)
