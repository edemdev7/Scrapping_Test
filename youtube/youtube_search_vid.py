import logging
from googleapiclient.discovery import build 
from openpyxl import Workbook

# Configuration du logging
logging.basicConfig(level=logging.INFO)

class YouTubeAPIWrapper:
    def __init__(self, api_key):
        self.api_key = api_key
        self.youtube = build('youtube', 'v3', developerKey=api_key)

    def search_videos(self, query):
        try:
            videos = []
            request = self.youtube.search().list(
                part='id,snippet',
                q=query,
                type='video',
                maxResults=100 # Nombre maximal de vidéos à récupérer
            )
            response = request.execute()
            for item in response['items']:
                video_id = item['id']['videoId']
                channel_id = item['snippet']['channelId']  # Récupération de l'ID de la chaîne
                video_snippet = item['snippet']
                video_stats = self.get_video_statistics(video_id)
                video_comments = self.get_video_comments(video_id)
                videos.append({'video_id': video_id, 'channel_id': channel_id, 'snippet': video_snippet, 'statistics': video_stats, 'comments': video_comments})
            return videos
        except Exception as e:
            logging.error(f"Une erreur s'est produite lors de la recherche de vidéos : {e}")
            return []

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

# Fonction pour enregistrer les résultats dans un fichier Excel
def save_to_excel(videos):
    wb = Workbook()
    ws = wb.active
    ws.append(['Chaîne ID', 'Video ID', 'Titre de la vidéo', 'Statistiques', 'Commentaires'])
    for video in videos:
        channel_id = video['channel_id']
        video_id = video['video_id']
        video_title = video['snippet']['title']
        video_statistics = str(video['statistics'])
        video_comments = '\n'.join(video['comments'])
        ws.append([channel_id, video_id, video_title, video_statistics, video_comments])
    wb.save('videos.xlsx')

# Exemple d'utilisation
if __name__ == "__main__":
    api_key = 'AIzaSyBe_qIQKc8DqyJp_Oilp8hofD3gABpbADw'
    youtube_api = YouTubeAPIWrapper(api_key)

    # Recherche de vidéos sur le football
    query = '#education#benin'
    benin_education_videos = youtube_api.search_videos(query)

    # Enregistrement des résultats dans un fichier Excel
    save_to_excel(benin_education_videos)
    logging.info("Les résultats ont été enregistrés dans le fichier 'videos.xlsx'.")
