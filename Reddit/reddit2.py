import praw
import pandas as pd

# Initialisation de l'instance Reddit
reddit = praw.Reddit(client_id='Pwp8F1QtppU6ZKE5c5221Q',
                     client_secret='_v42quaoSAYiakhW9W4tnjfibeLiKA',
                     user_agent='Scrapping')

# Initialisation de la liste pour stocker les données des posts
posts = []

# Récupération du subreddit "MachineLearning"
ml_subreddit = reddit.subreddit('MachineLearning')

# Parcours des 10 premiers posts chauds
for post in ml_subreddit.hot(limit=10):
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])

# Conversion en DataFrame pandas avec les noms des colonnes spécifiés
posts_df = pd.DataFrame(posts, columns=['Title', 'Score', 'ID', 'Subreddit', 'URL', 'Num_Comments', 'Body', 'Created'])

# Écriture dans un fichier Excel
posts_df.to_excel('top_ml_subreddit_posts.xlsx', index=False)

print("Fichier Excel 'top_ml_subreddit_posts.xlsx' créé avec succès.")
