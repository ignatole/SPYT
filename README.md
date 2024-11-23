# SPYT - Convertir Playlist de Spotify a YouTube

¿Tenés una playlist copada en Spotify y querés pasarla a YouTube? ¡Con SPYT lo podés hacer! Esta app toma una playlist de Spotify y la convierte en una playlist privada en tu canal de YouTube, buscando los videos correspondientes para cada canción. Es rápida y fácil de usar, ¡ideal para no perderte de la música que te gusta en ambas plataformas!

## Tecnologías utilizadas

- **Spotify API**: Para acceder a la playlist de Spotify y sacar las canciones.
- **YouTube API**: Para crear la playlist en YouTube y agregar los videos.
- **Python**: El lenguaje que se usa para todo esto.
- **OAuth 2.0**: Para autenticarte en ambas plataformas de forma segura.
- **Google API Client**: Para interactuar con la API de YouTube.

## Pasos para ejecutar la app

### 1. Cloná el repositorio

Primero, cloná el repositorio a tu máquina. En la terminal o CMD, ejecutá:
git clone https://github.com/ignatole/SPYT

### 2. Instalá las dependencias

Esta app usa algunas librerías que necesitarás instalar. Podés hacerlo con pip:
pip install -r requirements.txt

### 3. Conseguí las credenciales de Spotify y YouTube

#### Para Spotify:
1. Entrá a [Spotify Developer](https://developer.spotify.com/dashboard/applications) y logueate.
2. Crea una nueva app. Ahí vas a obtener tu **Client ID** y **Client Secret**.
3. Copialos y pegálos en el archivo `SPYT.py` en las siguientes variables:
    ```python
    SPOTIFY_CLIENT_ID = '@TU_CLIENT_ID_DE_SPOTIFY'
    SPOTIFY_CLIENT_SECRET = '@TU_CLIENT_SECRET_DE_SPOTIFY'
    SPOTIFY_REDIRECT_URI = '@TU_REDIRECT_URI'
    ```

#### Para YouTube:
1. Andá a la [Google Cloud Console](https://console.developers.google.com/).
2. Creá un nuevo proyecto y habilitá la API de YouTube Data v3.
3. Generá las credenciales OAuth 2.0 y descargá el archivo `credentials.json`.
4. Poné la ruta de ese archivo en la variable `CLIENT_SECRET_FILE` de `SPYT.py`:
    ```python
    CLIENT_SECRET_FILE = '@RUTA_DEL_ARCHIVO_CREDENTIALS_DE_YOUTUBE'
    ```

### 4. Ejecutá el script

Una vez configuradas las credenciales, ejecutá el script: python SPYT.py

El programa va a hacer lo siguiente:
- Te va a pedir que inicies sesión con tu cuenta de Spotify (si no lo hiciste antes).
- Después, te va a pedir permiso para acceder a tu cuenta de YouTube.
- Va a tomar las canciones de la playlist de Spotify que indiques y las va a buscar en YouTube.
- Finalmente, va a crear una playlist privada en tu canal de YouTube y va a agregar las canciones encontradas.

### 5. Personalizá tu playlist

En el archivo `SPYT.py`, podés modificar los siguientes valores:
- `playlist_id_spotify`: Poné el ID de la playlist de Spotify que querés convertir.
- `@NOMBRE_DE_LA_PLAYLIST`: El nombre que tendrá la playlist en YouTube.
- `@DESCRIPCION_DE_LA_PLAYLIST`: La descripción de la playlist.

### 6. ¿Algo no funciona?

Si no podés obtener las credenciales o algo no funciona, fijate que hayas seguido todos los pasos correctamente. Si el error persiste, fijate en la documentación de las [APIs de Spotify](https://developer.spotify.com/documentation/web-api/) y [YouTube](https://developers.google.com/youtube/v3) para más detalles.

## Aclaraciones

- La app crea playlists privadas en YouTube, para que no se haga pública la música que agregás.
- Si alguna canción no se encuentra en YouTube, el script te avisa, pero no la agrega.
- La primera vez que corras el script, va a necesitar que autorices a la app a acceder a tu cuenta de YouTube, pero solo es necesario hacer esto una vez.

## ¿Te gustó? ¡Contribuimos a que tu música fluya!

Si te gustaría mejorar la app, podés hacer un fork del repositorio y contribuir con nuevos features o reportar bugs.

---

**¡Disfrutá de tu música en YouTube y Spotify sin límites!**