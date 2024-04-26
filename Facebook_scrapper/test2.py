import requests

def get_education_pages(access_token, query='éducation Bénin'):
    base_url = 'https://graph.facebook.com/v12.0/search'
    params = {
        'q': query,
        'type': 'page',
        'access_token': access_token
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    if 'data' in data:
        return [page['name'] for page in data['data']]
    else:
        print("Erreur lors de la récupération des données:", data)
        return []

if __name__ == "__main__":
    access_token = 'EAAF6NyCLxZCkBO2olZBBv51o1ZBUaXTY7yxbsK1HPZCMD8t7DilnstsrZC0fTdoy5uocttPgXc5vJKQVZBvoYOq6zR1oKc1Lp0pSpnj4KJ8TVsrRS4zdZCGo8rJFY9Qm6u7gqTmZCguKl9kKtFPZAZCQ2csRzTAHBvdL1ZBsWaxyQ6SgVVx5S0OUxEu7Xh4g2Arq19WdUZA5EzFQDirZA18SHRAZDZD'
    education_pages = get_education_pages(access_token)
    print("Pages d'éducation au Bénin :")
    for page in education_pages:
        print(page)
