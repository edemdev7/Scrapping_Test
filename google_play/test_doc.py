import pandas as pd

# Données fournies
data = {
    "title": "Pokémon GO",
    "description": "New! Now you can battle other Pokémon GO Trainers online! Try the GO Battle League today!\r\n\r\nJoin Trainers across the globe who are discovering Pokémon as they explore the world around them. Pokémon GO is the global gaming sensation that has been downloaded over 1 billion times and named “Best Mobile Game” by the Game Developers Choice Awards and “Best App of the Year” by TechCrunch.\r\n_______________\r\n\r\nUncover the world of Pokémon: Explore and discover Pokémon wherever you are!\r\n \r\nCatch more Pokémon to complete your Pokédex!\r\n \r\nJourney alongside your Buddy Pokémon to help make your Pokémon stronger and earn rewards!\r\n\r\nCompete in epic Gym battles and...\r\n\r\nTeam up with other Trainers to catch powerful Pokémon during Raid Battles!\r\n \r\nIt’s time to get moving—your real-life adventures await! Let’s GO!\r\n_______________\r\n\r\nNotes: \r\n- This app is free-to-play and offers in-game purchases. It is optimized for smartphones, not tablets.\r\n- Compatible with Android devices that have 2GB RAM or more and have Android Version 6.0–10.0+ installed.\r\n- Compatibility is not guaranteed for devices without GPS capabilities or devices that are connected only to Wi-Fi networks.\r\n- Application may not run on certain devices even if they have compatible OS versions installed.\r\n- It is recommended to play while connected to a network in order to obtain accurate location information.\r\n- Compatibility information may be changed at any time.\r\n- Please visit PokemonGO.com for additional compatibility information. \r\n- Information current as of October 20, 2020.",
    "summary": "Discover Pokémon worldwide",
    "installs": "100,000,000+",
    "minInstalls": 100000000,
    "realInstalls": 449897250,
    "score": 4.28594,
    "ratings": 15214804,
    "reviews": 970851,
    "price": 0,
    "free": True,
    "currency": "USD",
    "offersIAP": True,
    "inAppProductPrice": "$0.99 - $99.99 per item",
    "developer": "Niantic, Inc.",
    "developerId": "Niantic,+Inc.",
    "developerEmail": "pokemon-go-support@nianticlabs.com",
    "developerWebsite": "https://niantic.helpshift.com/a/pokemon-go/?p=web",
    "developerAddress": "One Ferry Building, Suite 200\nSan Francisco, CA 94111",
    "privacyPolicy": "https://nianticlabs.com/privacy/pokemongo/en",
    "genre": "Adventure",
    "icon": "https://play-lh.googleusercontent.com/SVQIX_fYcu5mc4Pq-D7dgxXZdRMpNTAbRKeBJygAsIXKITHEcKckyhzLsIXMQLSRZw",
    "headerImage": "https://play-lh.googleusercontent.com/KgDQ-Kjb2B7_jDP-8KmQDNhAmP2lqAV_w3zArOCBL7YZnQ02Qqp4VTlgdocO-4MFk4s",
    "contentRating": "Everyone",
    "adSupported": False,
    "containsAds": False,
    "released": "Jul 6, 2016",
    "updated": 1654116395,
    "version": "0.239.1",
    "comments": [
        "5/12: crashes when i switch between screens, fold 3. Restarts each time, VERY annoying. It's a really fun game and I enjoy the aspect of going out for more than just a breath of fresh air. However, I'm on a Galaxy fold 3 common I find this game crashes quite often. What I mean is that it doesn't fully load when I open it. I've tried for stopping it, clearing cache, and even then it's hit or miss.",
        "The game itself is a great concept, and executed well. The community is still quite active(what, 4, 5 years later?) and is updated frequently. The issue is that there are a few really bad bugs.(I'll only be able to talk about one bug due to text limit :) ) This has only happened during the last week or so, where 4/5 times that I attempt to log in it stops at the very end. Then I have to exit out of the app and retry. This sometimes has taken up to 25 MINUTES to finally get a time where it works.",
        # Ajoutez d'autres commentaires ici...
    ]
}

# Création du DataFrame
df = pd.DataFrame({
    "Title": [data['title']],
    "Description": [data['description']],
    "Summary": [data['summary']],
    "Installs": [data['installs']],
    "Rating": [data['score']],
    "Reviews": [data['reviews']],
    "Developer": [data['developer']],
    "Developer Email": [data['developerEmail']],
    "Developer Website": [data['developerWebsite']],
    "Privacy Policy": [data['privacyPolicy']],
    "Genre": [data['genre']],
    "Content Rating": [data['contentRating']],
    "Ad Supported": [data['adSupported']],
    "Contains Ads": [data['containsAds']],
    "Released": [data['released']],
    "Updated": [data['updated']],
    "Version": [data['version']],
    "In-App Purchases": [data['offersIAP']],
    "In-App Product Price": [data['inAppProductPrice']]
})

# Ajout des commentaires au DataFrame
comments_df = pd.DataFrame({"Comments": data['comments']})
df['Comments'] = comments_df['Comments']

# Export des données vers un fichier Excel
df.to_excel("pokemon_go_data.xlsx", index=False)
