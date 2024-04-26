import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://www.linkedin.com/search/results/content/?keywords=education%20in%20benin&origin=SWITCH_SEARCH_VERTICAL&sid=s8h'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    article_listings = soup.find_all('div', {'class': 'content-hub-entities'})
    
    # Initialisation des listes pour stocker les données
    titles = []
    descriptions = []
    links = []

    for article in article_listings:
        title = article.find('h2', {'class': 'break-words'}).text.strip()
        description = article.find('p', {'class': 'content-description'}).text.strip()
        
        # Modification : Utilisation de article.find() au lieu de soup.find()
        anchor_tag = article.find('a', class_='min-w-0')
        
        # Modification : Vérification de l'existence de l'élément avant d'extraire l'attribut 'href'
        if anchor_tag:
            href_link = anchor_tag['href']
        else:
            href_link = "N/A"  # Si le lien n'est pas trouvé, nous définissons N/A
            
        # Ajout des données aux listes
        titles.append(title)
        descriptions.append(description)
        links.append(href_link)

    # Création d'un DataFrame pandas
    df = pd.DataFrame({
        'Title': titles,
        'Description': descriptions,
        'Article Link': links
    })

    # Exportation du DataFrame vers un fichier Excel
    df.to_excel('article_linkedin.xlsx', index=False)
    print("Data saved to 'article_linkedin.xlsx' successfully.")
else:
    print("Failed to fetch article listings.")
