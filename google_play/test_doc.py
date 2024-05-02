from google_play_scraper import Sort, reviews

result, continuation_token = reviews(
    'bj.sbin.mobilemoney.customer',
    lang='fr', # Language in which to fetch reviews
    country='bj', # Country to which the reviews pertain
    sort=Sort.NEWEST, # Sorting order
    count=150
)


for review in result:
    print(review)