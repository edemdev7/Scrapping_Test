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
    access_token = 'EAAFdqMwm1CgBO2B9ezAn7TWZCNmOrZCrdyNoZAYjYeCknb951OLuqArUEJq9J4dppBbLKc6z3MlMPJbq6MifdU7WDolZCRDK8jJgVy9zZCvc3V4Nm3m6C2nkax1c7NIx9zKrNZAnmP9ptgfhmvSZBUnUx1fx0PQCFoYOoCCP1U4Am3XwLuxgiku9F9SHoIIOiZACuprqMpOWCvunazZBt8iizaFAlmbQ8nU82WIdZBfwdPB1fTnjZBO7ntdDAZDZD'  
    comments = get_facebook_post_comments(post_id, access_token)
    for comment in comments:
        print("Auteur du commentaire:", comment['from']['name'])
        print("Contenu du commentaire:", comment['message'])
        print('---')
