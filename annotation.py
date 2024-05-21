import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder

# Charger le fichier Excel
def annotate_excel(file_path, model, tokenizer, label_encoder, max_sequence_length):
    # Charger le fichier Excel dans un DataFrame
    df = pd.read_excel(file_path)

    # Vérifier que la colonne 'texte' existe dans le DataFrame
    if 'texte' not in df.columns:
        raise ValueError("Le fichier Excel doit contenir une colonne 'texte'.")

    # Définir une fonction pour prédire le sentiment d'un texte
    def predict_sentiment(text):
        # Tokeniser et padder le texte d'entrée
        sequence = tokenizer.texts_to_sequences([text])
        padded_sequence = pad_sequences(sequence, maxlen=max_sequence_length, padding='post')

        # Prédire le sentiment
        predicted_prob = model.predict(padded_sequence)[0][0]

        # Convertir la probabilité prédite en label
        predicted_label = 1 if predicted_prob >= 0.5 else 0

        # Convertir le label en catégorie de sentiment
        sentiment_category = label_encoder.inverse_transform([predicted_label])[0]

        return sentiment_category

    # Appliquer la fonction de prédiction sur chaque texte et ajouter les prédictions dans une nouvelle colonne
    df['sentiment'] = df['texte'].apply(predict_sentiment)

    # Enregistrer le fichier Excel annoté avec les prédictions
    output_file_path = file_path.replace('.xlsx', '_annotated.xlsx')
    df.to_excel(output_file_path, index=False)

    print(f"Le fichier annoté a été enregistré sous {output_file_path}")

# Exemple d'utilisation
file_path = "votre_fichier.xlsx"

# Assurez-vous que ces variables sont définies selon votre contexte d'entraînement de modèle
# tokenizer, label_encoder, model, max_sequence_length

annotate_excel(file_path, model, tokenizer, label_encoder, max_sequence_length)
