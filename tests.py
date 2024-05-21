import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Embedding

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
#model.fit(X_train_padded, y_train, epochs=10, batch_size=32)
history = model.fit(X_train_padded, y_train, validation_split=0.2, epochs=10, batch_size=32)

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
 

def predict_sentiment(text, model, tokenizer, label_encoder):
    # Tokenize and pad the input text
    sequence = tokenizer.texts_to_sequences([text])
    padded_sequence = pad_sequences(sequence, maxlen=max_sequence_length, padding='post')
    
    # Predict the sentiment label
    predicted_prob = model.predict(padded_sequence)[0][0]
    
    # Convert predicted probability to label
    predicted_label = 1 if predicted_prob >= 0.5 else 0
    
    # Convert label to sentiment category
    sentiment_category = label_encoder.inverse_transform([predicted_label])[0]
    
    return sentiment_category

text = ""
predicted_label = predict_sentiment(text, model, tokenizer, label_encoder)
print("Predicted sentiment:", predicted_label)
"""

def predict_sentiment(text, model, tokenizer, label_encoder):
    if not isinstance(text, str):
        return None  # Skip or handle non-string values appropriately
    
    # Tokenize and pad the input text
    sequence = tokenizer.texts_to_sequences([text])
    padded_sequence = pad_sequences(sequence, maxlen=max_sequence_length, padding='post')
    
    # Predict the sentiment label
    predicted_prob = model.predict(padded_sequence)[0][0]
    
    # Convert predicted probability to label
    predicted_label = 1 if predicted_prob >= 0.5 else 0
    
    # Convert label to sentiment category
    sentiment_category = label_encoder.inverse_transform([predicted_label])[0]
    
    return sentiment_category

def annotate_excel_file(input_file, output_file):
    # Load the Excel file into a pandas DataFrame
    df = pd.read_excel(input_file)
    
    # Ensure the text column is named 'texte_nettoye'
    if 'texte_nettoye' not in df.columns:
        raise ValueError("The input Excel file must contain a column named 'texte_nettoye'.")

    # Iterate over each row and predict the sentiment
    df['sentiment'] = df['texte_nettoye'].apply(lambda text: predict_sentiment(text, model, tokenizer, label_encoder))

    # Save the updated DataFrame back to an Excel file
    df.to_excel(output_file, index=False)

# Example usage
input_file = '/home/edemdev/Edem/Stage/PYTHON_NPL/Scrapping_Test/Dataset_nettoye/Mtn_app.xlsx'
output_file = 'output_file.xlsx'
annotate_excel_file(input_file, output_file)
