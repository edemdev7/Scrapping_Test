import logging
from googleapiclient.discovery import build 

# Configuration du logging
logging.basicConfig(level=logging.INFO)

class YouTubeAPIWrapper:
    def __init__(self, api_key):
        self.api_key = api_key
        self.youtube = build('youtube', 'v3', developerKey=api_key)

    def get_channel_statistics(self, username):
        try:
            request = self.youtube.channels().list(
                part='statistics',
                forUsername=username
            )
            response = request.execute()
            return response['items'][0]['statistics']
        except Exception as e:
            logging.error(f"Une erreur s'est produite lors de la récupération des statistiques de la chaîne : {e}")
            return None

# Exemple d'utilisation
if __name__ == "__main__":
    api_key = 'AIzaSyBe_qIQKc8DqyJp_Oilp8hofD3gABpbADw'
    youtube_api = YouTubeAPIWrapper(api_key)

    # Récupération des statistiques de la chaîne
    username = 'BBCNews'
    channel_statistics = youtube_api.get_channel_statistics(username)
    if channel_statistics:
        logging.info(f"Statistiques de la chaîne '{username}': {channel_statistics}")
    else:
        logging.warning(f"Impossible de récupérer les statistiques de la chaîne '{username}'.")
