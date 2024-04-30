import logging
from googleapiclient.discovery import build 

# Configuration du logging
logging.basicConfig(level=logging.INFO)

class YouTubeAPIWrapper:
    def __init__(self, api_key):
        self.api_key = api_key
        self.youtube = build('youtube', 'v3', developerKey=api_key)

    def get_video_statistics(self, video_id):
        try:
            request = self.youtube.videos().list(
                part='statistics',
                id=video_id
            )
            response = request.execute()
            return response['items'][0]['statistics']
        except Exception as e:
            logging.error(f"Une erreur s'est produite lors de la récupération des statistiques de la vidéo : {e}")
            return None

    def get_video_comments(self, video_id):
        try:
            comments = []
            request = self.youtube.commentThreads().list(
                part='snippet',
                videoId=video_id,
                maxResults=100  # Nombre maximal de commentaires à récupérer
            )
            while request:
                response = request.execute()
                for item in response['items']:
                    comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                    comments.append(comment)
                request = self.youtube.commentThreads().list_next(request, response)
            return comments
        except Exception as e:
            logging.error(f"Une erreur s'est produite lors de la récupération des commentaires de la vidéo : {e}")
            return []

# Exemple d'utilisation
if __name__ == "__main__":
    api_key = 'AIzaSyBe_qIQKc8DqyJp_Oilp8hofD3gABpbADw'
    youtube_api = YouTubeAPIWrapper(api_key)

    # Identifiant de la vidéo
    video_id = '22Ee9ayzfTU'

    # Récupération des statistiques de la vidéo
    video_statistics = youtube_api.get_video_statistics(video_id)
    if video_statistics:
        logging.info(f"Statistiques de la vidéo '{video_id}': {video_statistics}")
    else:
        logging.warning(f"Impossible de récupérer les statistiques de la vidéo '{video_id}'.")

    # Récupération des commentaires de la vidéo
    video_comments = youtube_api.get_video_comments(video_id)
    if video_comments:
        logging.info(f"Commentaires de la vidéo '{video_id}': {video_comments}")
    else:
        logging.warning(f"Aucun commentaire trouvé pour la vidéo '{video_id}'.")
