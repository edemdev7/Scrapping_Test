import requests
import pandas as pd

def get_facebook_posts_with_comments(page_id, access_token):
    base_url = f'https://graph.facebook.com/{page_id}/posts'
    params = {
        'access_token': access_token,
        'fields': 'id,message,created_time,comments.limit(5){message,created_time}',
        'limit': 5
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    posts_with_comments = []
    if 'data' in data:
        for post in data['data']:
            post_data = {
                'Post Message': post.get('message', 'N/A'),
                'Post Date': post.get('created_time', 'N/A')
            }
            comments = post.get('comments', {}).get('data', [])
            for comment in comments:
                post_data[f'Comment {comments.index(comment) + 1}'] = comment.get('message', 'N/A')
            posts_with_comments.append(post_data)
    else:
        print("Erreur lors de la récupération des données:", data)
    return posts_with_comments

if __name__ == "__main__":
    page_id = '109767023960819'
    access_token ='EAAF6NyCLxZCkBO02uNPMEt1NxmX8sSSyUswZBKNk7uGhlRPeIQME3ETwOqc1bwyiFacaXEZBqgff4SdK7HURIa2Kg1wPMiGCAiwZBw242rzcbwrPAh4CiV7ZAAenfXSzZAcTGh298iHmgTQpmPRAPZAUiZAlVdxiEPLq7aC7JdPB0GZCtHupZAxkZCQcxjSZBK1zZCrIscDSuCx390tOp4AGTVt4X40w1Yi0ZD'
    
    posts_with_comments = get_facebook_posts_with_comments(page_id, access_token)
    
    # Conversion en DataFrame pandas
    df = pd.DataFrame(posts_with_comments)
    
    # Écriture dans un fichier Excel
    df.to_excel('facebook_posts_with_comments.xlsx', index=False)

    print("Fichier Excel 'facebook_posts_with_comments.xlsx' créé avec succès.")
