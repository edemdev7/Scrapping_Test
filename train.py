import pandas as pd
import numpy as np

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from keras.layers import Input, LSTM, Embedding, Dense, Concatenate
from keras.models import Model

# Charger les données
data = pd.read_csv("train_sortie.csv")

# Remplir les valeurs manquantes avec des chaînes vides
data['text'].fillna('', inplace=True)
data['selected_text'].fillna('', inplace=True)

# Convertir les étiquettes de sentiment en valeurs numériques
label_encoder = LabelEncoder()
data['sentiment'] = label_encoder.fit_transform(data['sentiment'])

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(data[['text', 'selected_text']], data['sentiment'], test_size=0.2, random_state=42)

# Tokenisation et vectorisation du texte
tokenizer = Tokenizer()
tokenizer.fit_on_texts(X_train['text'].tolist() + X_train['selected_text'].tolist())

X_train_text_sequences = tokenizer.texts_to_sequences(X_train['text'])
X_train_selected_text_sequences = tokenizer.texts_to_sequences(X_train['selected_text'])
X_test_text_sequences = tokenizer.texts_to_sequences(X_test['text'])
X_test_selected_text_sequences = tokenizer.texts_to_sequences(X_test['selected_text'])

# Rembourrage des séquences pour qu'elles aient la même longueur
max_sequence_length = max([len(seq) for seq in X_train_text_sequences + X_train_selected_text_sequences])
X_train_text_padded = pad_sequences(X_train_text_sequences, maxlen=max_sequence_length, padding='post')
X_train_selected_text_padded = pad_sequences(X_train_selected_text_sequences, maxlen=max_sequence_length, padding='post')
X_test_text_padded = pad_sequences(X_test_text_sequences, maxlen=max_sequence_length, padding='post')
X_test_selected_text_padded = pad_sequences(X_test_selected_text_sequences, maxlen=max_sequence_length, padding='post')

# Définir les entrées nommées
text_input = Input(shape=(max_sequence_length,), name='text_input')
selected_text_input = Input(shape=(max_sequence_length,), name='selected_text_input')

# Embedding pour chaque entrée
text_embedding = Embedding(input_dim=len(tokenizer.word_index)+1, output_dim=100)(text_input)
selected_text_embedding = Embedding(input_dim=len(tokenizer.word_index)+1, output_dim=100)(selected_text_input)

# LSTM pour chaque entrée
text_lstm = LSTM(64)(text_embedding)
selected_text_lstm = LSTM(64)(selected_text_embedding)

# Concaténer les sorties LSTM
concatenated_output = Concatenate()([text_lstm, selected_text_lstm])

# Sortie pour la prédiction du sentiment
sentiment_output = Dense(1, activation='sigmoid', name='sentiment_output')(concatenated_output)

# Sortie pour la prédiction du texte sélectionné
selected_text_output = Dense(max_sequence_length, activation='softmax', name='selected_text_output')(concatenated_output)

# Créer le modèle en spécifiant les entrées et les sorties
model = Model(inputs={'text_input': text_input, 'selected_text_input': selected_text_input},
              outputs={'sentiment_output': sentiment_output, 'selected_text_output': selected_text_output})

# Compiler le modèle avec des pertes et des métriques appropriées pour chaque sortie
model.compile(optimizer='adam',
              loss={'sentiment_output': 'binary_crossentropy', 'selected_text_output': 'categorical_crossentropy'},
              metrics={'sentiment_output': 'accuracy', 'selected_text_output': 'accuracy'})

# Entraîner le modèle en passant les données dans un dictionnaire spécifiant les noms des entrées
history = model.fit({'text_input': X_train_text_padded, 'selected_text_input': X_train_selected_text_padded},
                    {'sentiment_output': y_train, 'selected_text_output': np.array(X_train_selected_text_sequences)},
                    epochs=10, batch_size=32,
                    validation_data=({'text_input': X_test_text_padded, 'selected_text_input': X_test_selected_text_padded},
                                     {'sentiment_output': y_test, 'selected_text_output': np.array(X_test_selected_text_sequences)}))
