import requests

def get_page_ids_by_topic(topic, access_token):
    # Définissez l'URL de base pour l'API Graph
    base_url = "https://developers.facebook.com/tools/explorer"

    # Construisez la requête de recherche
    search_query = f"/search?q={topic}&type=page"

    # Construisez l'URL complet
    url = f"{base_url}{search_query}&access_token={access_token}"

    try:
        # Envoyez une requête GET à l'API Graph
        response = requests.get(url)
        data = response.json()

        # Extrait les IDs des pages à partir de la réponse
        page_ids = [page["id"] for page in data.get("data", [])]

        return page_ids

    except requests.RequestException as e:
        print(f"Erreur lors de la récupération des données depuis l'API Graph de Facebook : {e}")
        return []

# Définissez votre jeton d'accès Facebook
access_token = "EAAFdqMwm1CgBOZBq9S4eBVImM9zFWKMYiHNBKBouUafcZBCXurpqMphEvr2zE4iZAmkzmaplrbsZAWhOZClrO91JPWlCX9bpuFqH96acT5FR7wVCgqBJtjN0Q7w50ha2snB6UCjvQGwqDbi99PntBohZCnLNRLe7xM8tR3tMam6uYtZC63F7FXcNTmZCaAyEpYTu6giZAaCms7ZCXLj9sPgZBgwfGyix9cR1LZAZALoHvRa6pZAMTdfV9RHn6NPxZAAymFufgZDZD"

# Définissez la thématique que vous souhaitez rechercher (par exemple, "musique")
topic_to_search = "musique"

# Obtenez les IDs des pages liées à la thématique
page_ids = get_page_ids_by_topic(topic_to_search, access_token)

# Affichez les IDs des pages
print(f"IDs des pages liées à '{topic_to_search}':")
for page_id in page_ids:
    print(page_id)
