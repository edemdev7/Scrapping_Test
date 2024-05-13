import pandas as pd

# Charger le fichier Excel
df = pd.read_excel("/home/edemdev/Edem/Stage/PYTHON_NPL/Scrapping_Test/Datasets/celtiis_benin.xlsx")

# Remplacer les valeurs manquantes dans la colonne "text" par les valeurs de la colonne "content"
df["text"] = df["text"].fillna(df["content"])

# Afficher les premières lignes du dataframe avec la colonne "text" fusionnée
print(df.head())


# Enregistrer le DataFrame modifié dans un nouveau fichier Excel
df.to_excel("nouveau_fichier.xlsx", index=False)
