import requests

def get_facebook_post_comments(post_id, access_token):
    base_url = f'https://graph.facebook.com/{post_id}/comments'
    params = {
        'access_token': access_token,
        'fields': 'message,from',
        'limit': 100
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    if 'data' in data:
        return data['data']
    else:
        print("Erreur lors de la récupération des commentaires:", data)
        return []

if __name__ == "__main__":
    post_id = '1501982113998604_1493759814820834' 
    access_token = 'EAAFdqMwm1CgBO1fZAz6ObBoQ50OWIYiokPs4vTF3SwhHr0mJRoihmPtYZAnImLvg9mah4p4tqXz1aujIdN8fZBV0c0YyQ3ZBDjjzfd4SIwahf1VObZAu3pBs7w45ZAXKJDhqIVlglCtXkaaETR9vNyiu0lfuPntzVniupv75l9mLIZAZBadIrsq0inWJnEywN7OaXfJ6ArAICITJjCY8KZBhORuNBXWYs6LVyMSwqZAq7lZC5cjT9BPJkwn'  
    comments = get_facebook_post_comments(post_id, access_token)
    for comment in comments:
        print("Auteur du commentaire:", comment['from']['name'])
        print("Contenu du commentaire:", comment['message'])
        print('---')
