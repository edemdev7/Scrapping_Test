import requests

# Identifiants d'application Pinterest
client_id = '1498197'
client_secret = 'pina_AMAVLXAWACGD2AYAGDAGYDG52JCAXDYBQBIQCRTKGDD2T45LE5MQ26NXYIG2T36CLXZPTL64RVZBSERL7BPMCUHNRP5APFIA'

# Paramètres de recherche
query = 'education in Benin'

# Endpoint de recherche de pins
search_endpoint = 'https://api.pinterest.com/v5/queries/search/pins/'

# Paramètres de requête
params = {
    'access_token': f'{client_id}:{client_secret}',
    'query': query
}

# Effectuer la requête HTTP GET
response = requests.get(search_endpoint, params=params)

# Vérifier le code d'état de la réponse
if response.status_code == 200:
    # Récupérer les résultats de recherche sous forme de JSON
    search_results = response.json()
    
    # Afficher les résultats de recherche
    for pin in search_results['data']:
        print(pin['query'])
else:
    print('Failed to fetch search results.')
