import praw
import pandas as pd

# Initialisation de l'instance Reddit
reddit = praw.Reddit(client_id='Pwp8F1QtppU6ZKE5c5221Q',
                     client_secret='_v42quaoSAYiakhW9W4tnjfibeLiKA',
                     user_agent='Scrapping')

# Fonction pour récupérer le contenu des commentaires d'un post
def get_comments(post):
    comments_list = []
    post.comments.replace_more(limit=None)  # Récupère tous les commentaires, y compris les réponses en profondeur
    for comment in post.comments.list():
        comments_list.append(comment.body)
    return '\n\n'.join(comments_list)

# Initialisation de la liste pour stocker les données des posts et des commentaires
posts = []

# Récupération du subreddit "MachineLearning"
ml_subreddit = reddit.subreddit('MachineLearning')

# Parcours des 10 premiers posts chauds
for post in ml_subreddit.hot(limit=10):
    post_data = [post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created, get_comments(post)]
    posts.append(post_data)

# Conversion en DataFrame pandas avec les noms des colonnes spécifiés
posts_df = pd.DataFrame(posts, columns=['Title', 'Score', 'ID', 'Subreddit', 'URL', 'Num_Comments', 'Body', 'Created', 'Comments'])

# Écriture dans un fichier Excel
posts_df.to_excel('reddit_benineduc.xlsx', index=False)

print("Fichier Excel '_posts_with_comments.xlsx' créé avec succès.")
