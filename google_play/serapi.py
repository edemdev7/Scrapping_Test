import serpapi
import os
import pandas as pd 

api_key='c3932ec9b0bc24e2b23f548da05d4e466f9b647b99baae639ff9e779bc76f29d'
client=serpapi.Client(api_key=api_key)

results = client.search(
    engine="google_play_product",
    product_id="com.mtn.agentapp",
    store="apps",
    all_reviews="true",
    num=10
)


data = results['reviews']
df = pd.DataFrame(data)

excel_file = "mtn_agent.xlsx"
df.to_excel(excel_file, index=False)

print(f"Avis de l'application enregistrés dans le fichier Excel : {excel_file}")
