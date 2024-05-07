from google_play_scraper import app

import pandas as pd

import numpy as np 

from google_play_scraper import Sort, reviews_all


us_reviews = reviews_all(
    'com.tlc.etisalat.flooz.agent.ga',
    sleep_milliseconds=0, # defaults to 0
    lang='fr', # defaults to 'en'
    country='bj', # defaults to 'us'
    sort=Sort.NEWEST, # defaults to Sort.MOST_RELEVANT
    
) 

df_busu = pd.DataFrame(np.array(us_reviews),columns=['review'])
df_busu = df_busu.join(pd.DataFrame(df_busu.pop('review').tolist()))
df_busu.head() 

excel_file = "moov_tgBJ.xlsx"
df_busu.to_excel(excel_file, index=False)