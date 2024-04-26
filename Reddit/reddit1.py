import praw
reddit = praw.Reddit(client_id='Pwp8F1QtppU6ZKE5c5221Q',client_secret='_v42quaoSAYiakhW9W4tnjfibeLiKA',user_agent='Scrapping')

# get 10 hot posts from the MachineLearning subreddit
#hot_posts = reddit.subreddit('MachineLearning').hot(limit=10)

# get hot posts from all subreddits
hot_posts = reddit.subreddit('all').hot(limit=10)

# Now that we scraped 10 posts we can loop through them and print some information.

for post in hot_posts:
    print(post.title)

# get MachineLearning subreddit data
ml_subreddit = reddit.subreddit('Education')

print(ml_subreddit.description)