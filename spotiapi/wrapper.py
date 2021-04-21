from http3 import AsyncClient


class SpotifyAPIWrapper:
    def __init__(self, authorization_token: str):
        self.token = authorization_token
        self.request_module = AsyncClient()

    async def get_player(self):
        """
        This function returns the current track and the artist that the user is currently listening to.
        Requires the user-read-currently-playing parameter enabled in the Spotify API.

        @:return Current Player
        """
        request_headers = {'Authorization': f'Bearer {self.token}'}
        request_api = await self.request_module.get(url='https://api.spotify.com/v1/me/player/currently-playing',
                                                    headers=request_headers)
        request_api = request_api.json()

        try:
            is_playing = False
            if request_api['is_playing']:
                is_playing = True

            song_artists = []
            for artist in request_api['item']['artists']:
                song_artists.append(artist['name'])
        except:
            raise ValueError('The selected Spotify token is invalid, or an external error occurred on the server.')

        return {'is_playing': is_playing, 'player_artists': song_artists, 'player_name': request_api['item']}

    async def get_liked_albums(self):
        """
        The function returns all the albums that the user added to liked, or None if no albums were added.

        @:return: User Liked Albums
        """
        request_headers = {'Authorization': f'Bearer {self.token}'}
        request_api = await self.request_module.get(url='https://api.spotify.com/v1/me/albums', headers=request_headers)
        request_api = request_api.json()

        try:
            liked_albums = []
            if 'items' not in request_api:
                liked_albums = None

            for album_data in request_api['items']:
                if album_data['album']['album_type'] != 'album':
                    continue
                else:
                    liked_albums.append({'name': album_data['album']['name'], 'data': album_data['album']})
        except:
            raise ValueError('The selected Spotify token is invalid, or an external error occurred on the server.')

        return liked_albums

    async def get_playlists(self):
        """
        This function returns a list of playlists that the user has created or added to important ones.
        Requires the playlist-read-private parameter enabled in the Spotify API.

        @:return: User Playlists
        """
        request_headers = {'Authorization': f'Bearer {self.token}'}
        request_api = await self.request_module.get(url='https://api.spotify.com/v1/me/playlists',
                                                    headers=request_headers)
        request_api = request_api.json()

        try:
            user_playlists = []

            if 'items' not in request_api:
                user_playlists = None

            for playlist in request_api['items']:
                user_playlists.append({'name': playlist['name'], 'id': playlist['id']})
        except:
            raise ValueError('The selected Spotify token is invalid, or an external error occurred on the server.')

        return user_playlists

    async def get_self(self):
        """
        This function returns a user data object.
        Requires the user-read-private & user-read-email enabled in the Spotify API.

        @:return: Self User
        """
        try:
            request_headers = {'Authorization': f'Bearer {self.token}'}
            request_api = await self.request_module.get(url='https://api.spotify.com/v1/me', headers=request_headers)
            request_api = request_api.json()
        except:
            raise ValueError('The selected Spotify token is invalid, or an external error occurred on the server.')

        return request_api
