import requests

def get_facebook_posts(page_id, access_token):
    base_url = f'https://graph.facebook.com/{page_id}/posts'
    params = {
        'access_token': access_token,
        'fields': 'id,message,created_time,reactions.summary(total_count),shares',
        'limit': 10
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    if 'data' in data:
        return data['data']
    else:
        print("Erreur lors de la récupération des données:", data)
        return []

def display_post_info(post):
    print("Message:", post.get('message', 'N/A'))
    print("Date de création:", post.get('created_time', 'N/A'))
    reactions = post.get('reactions', {}).get('summary', {}).get('total_count', 0)
    print("Nombre total de réactions:", reactions)
    shares = post.get('shares', {}).get('count', 0)
    print("Nombre total de partages:", shares)

if __name__ == "__main__":
    page_id = '1501982113998604'
    access_token = 'EAAFdqMwm1CgBO2B9ezAn7TWZCNmOrZCrdyNoZAYjYeCknb951OLuqArUEJq9J4dppBbLKc6z3MlMPJbq6MifdU7WDolZCRDK8jJgVy9zZCvc3V4Nm3m6C2nkax1c7NIx9zKrNZAnmP9ptgfhmvSZBUnUx1fx0PQCFoYOoCCP1U4Am3XwLuxgiku9F9SHoIIOiZACuprqMpOWCvunazZBt8iizaFAlmbQ8nU82WIdZBfwdPB1fTnjZBO7ntdDAZDZD'
    posts = get_facebook_posts(page_id, access_token)
    for post in posts:
        display_post_info(post)
        print('---')
