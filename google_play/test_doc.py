from google_play_scraper import Sort, reviews
import pandas as pd

import numpy as np 


result, continuation_token = reviews(
    'com.mtn.mtnbjr3',
    lang='fr', # Language in which to fetch reviews
    country='bj', # Country to which the reviews pertain
    sort=Sort.NEWEST, # Sorting order
    count=100
)



df_busu = pd.DataFrame(np.array(result),columns=['review'])
df_busu = df_busu.join(pd.DataFrame(df_busu.pop('review').tolist()))
df_busu.head() 

excel_file = "mymtn_ap.xlsx"
df_busu.to_excel(excel_file, index=False)