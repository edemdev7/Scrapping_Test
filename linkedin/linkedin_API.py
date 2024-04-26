import requests
from urllib.parse import urlencode
from flask import Flask, request, redirect

# Informations de l'application LinkedIn
CLIENT_ID = '78h6noshr58xo9'
CLIENT_SECRET = 'LOZv2gDrHGYIwTtr'
REDIRECT_URI = 'http://localhost:5000/callback'
SCOPE = ' w_member_social'

# Création de l'application Flask
app = Flask(__name__)

# URL d'autorisation OAuth 2.0 de LinkedIn
AUTHORIZATION_URL = 'https://www.linkedin.com/oauth/v2/authorization?' + \
                    urlencode({
                        'response_type': 'code',
                        'client_id': CLIENT_ID,
                        'redirect_uri': REDIRECT_URI,
                        'scope': SCOPE
                    })

# Page de redirection après autorisation LinkedIn
@app.route('/callback')
def callback():
    code = request.args.get('code')

    # Échange du code d'autorisation contre un jeton d'accès
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }
    response = requests.post('https://www.linkedin.com/oauth/v2/accessToken', data=data)

    if response.status_code == 200:
        access_token = response.json()['access_token']
        return search_linkedin('éducation', access_token)
    else:
        return 'Erreur lors de l\'échange du code d\'autorisation contre un jeton d\'accès'

# Fonction de recherche LinkedIn
def search_linkedin(keyword, access_token):
    # Endpoint de recherche LinkedIn
    url = f'https://api.linkedin.com/v2/search?q={keyword}&start=0&count=10'

    # Envoi de la requête GET à l'API LinkedIn avec le jeton d'accès
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(url, headers=headers)

    # Traitement de la réponse de recherche
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return 'Échec de la recherche'

# Point d'entrée principal de l'application Flask
if __name__ == '__main__':
    # Lancement de l'application Flask
    app.run(debug=True)
