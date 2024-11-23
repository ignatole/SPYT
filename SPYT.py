import spotipy
from spotipy.oauth2 import SpotifyOAuth
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pickle
import os

SPOTIFY_CLIENT_ID = '@TU_CLIENT_ID_DE_SPOTIFY'
SPOTIFY_CLIENT_SECRET = '@TU_CLIENT_SECRET_DE_SPOTIFY'
SPOTIFY_REDIRECT_URI = '@TU_REDIRECT_URI'

CLIENT_SECRET_FILE = '@RUTA_DEL_ARCHIVO_CREDENTIALS_DE_YOUTUBE'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="playlist-read-private"
))

def obtener_canciones_playlist(playlist_id):
    resultados = spotify.playlist_tracks(playlist_id)
    canciones = []
    for item in resultados['items']:
        track = item['track']
        canciones.append(f"{track['name']} {track['artists'][0]['name']}")
    return canciones

def obtener_credenciales_youtube():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=8080)
        
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds

def crear_playlist_youtube(title, description):
    creds = obtener_credenciales_youtube()
    youtube = build(API_NAME, API_VERSION, credentials=creds)
    request = youtube.playlists().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
                "tags": ["Music", "Spotify", "YouTube"],
                "defaultLanguage": "en"
            },
            "status": {
                "privacyStatus": "private"
            }
        }
    )
    response = request.execute()
    return response["id"]

def buscar_en_youtube(query):
    creds = obtener_credenciales_youtube()
    youtube = build(API_NAME, API_VERSION, credentials=creds)
    request = youtube.search().list(
        q=query,
        part="snippet",
        maxResults=1
    )
    response = request.execute()
    return response['items'][0]['id']['videoId'] if response['items'] else None

def agregar_canciones_a_playlist_youtube(playlist_id, video_id):
    creds = obtener_credenciales_youtube()
    youtube = build(API_NAME, API_VERSION, credentials=creds)
    request = youtube.playlistItems().insert(
        part="snippet",
        body={
            "snippet": {
                "playlistId": playlist_id,
                "resourceId": {
                    "kind": "youtube#video",
                    "videoId": video_id
                }
            }
        }
    )
    request.execute()

if __name__ == "__main__":
    playlist_id_spotify = '@ID_DE_LA_PLAYLIST_DE_SPOTIFY'
    canciones = obtener_canciones_playlist(playlist_id_spotify)

    playlist_id_youtube = crear_playlist_youtube('@NOMBRE_DE_LA_PLAYLIST', '@DESCRIPCION_DE_LA_PLAYLIST')

    for cancion in canciones:
        video_id = buscar_en_youtube(cancion)
        if video_id:
            agregar_canciones_a_playlist_youtube(playlist_id_youtube, video_id)
            print(f"Añadida: {cancion}")
        else:
            print(f"No encontrada: {cancion}")

    print("¡Playlist creada con éxito en YouTube!")
