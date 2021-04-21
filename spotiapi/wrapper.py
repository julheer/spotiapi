# -*- coding: utf-8 -*-
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
        if int(request_api.status_code) != 200:
            return {'error': True, 'code': int(request_api.status_code)}
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
        if int(request_api.status_code) != 200:
            return {'error': True, 'code': int(request_api.status_code)}
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
        if int(request_api.status_code) != 200:
            return {'error': True, 'code': int(request_api.status_code)}
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
            if int(request_api.status_code) != 200:
                return {'error': True, 'code': int(request_api.status_code)}
            request_api = request_api.json()
        except:
            raise ValueError('The selected Spotify token is invalid, or an external error occurred on the server.')

        return request_api

    async def get_playlist_by_id(self, playlist_id: str = None):
        if playlist_id is None:
            raise AttributeError('This method requires the playlist ID to be specified.')

        try:
            request_headers = {'Authorization': f'Bearer {self.token}'}
            request_api = await self.request_module.get(url=f'https://api.spotify.com/v1/albums/{playlist_id}',
                                                        headers=request_headers)
            if int(request_api.status_code) != 200:
                return {'error': True, 'code': int(request_api.status_code)}
            request_api = request_api.json()
        except:
            raise ValueError('The selected Spotify token is invalid, or an external error occurred on the server.')

        return request_api

    async def get_playlist_tracks(self, playlist_id: str = None, offset: int = 0, limit: str = 20):
        if playlist_id is None:
            raise AttributeError('This method requires the playlist ID to be specified.')

        try:
            request_headers = {'Authorization': f'Bearer {self.token}'}
            request_api = await self.request_module.get(url=f'https://api.spotify.com/v1/albums/{playlist_id}/tracks'
                                                            f'?offset={offset}&limit={limit}',
                                                        headers=request_headers)
            if int(request_api.status_code) != 200:
                return {'error': True, 'code': int(request_api.status_code)}
            request_api = request_api.json()
        except:
            raise ValueError('The selected Spotify token is invalid, or an external error occurred on the server.')

        return request_api

    async def get_artist(self, artist_id: str = None):
        if artist_id is None:
            raise AttributeError('This method requires the artist ID to be specified.')

        try:
            request_headers = {'Authorization': f'Bearer {self.token}'}
            request_api = await self.request_module.get(url=f'https://api.spotify.com/v1/artists/{artist_id}',
                                                        headers=request_headers)
            if int(request_api.status_code) != 200:
                return {'error': True, 'code': int(request_api.status_code)}
            request_api = request_api.json()
        except:
            raise ValueError('The selected Spotify token is invalid, or an external error occurred on the server.')

        return request_api

    async def get_artist_top_songs(self, artist_id: str = None, country: str = 'ru'):
        if artist_id is None:
            raise AttributeError('This method requires the artist ID to be specified.')

        try:
            request_headers = {'Authorization': f'Bearer {self.token}'}
            request_api = await self.request_module.get(url='https://api.spotify.com/v1/artists/'
                                                            f'{artist_id}/top-tracks?country={country}',
                                                        headers=request_headers)
            if int(request_api.status_code) != 200:
                return {'error': True, 'code': int(request_api.status_code)}
            request_api = request_api.json()
        except:
            raise ValueError('The selected Spotify token is invalid, or an external error occurred on the server.')

        return request_api

    async def get_artist_related(self, artist_id: str = None):
        if artist_id is None:
            raise AttributeError('This method requires the artist ID to be specified.')

        try:
            request_headers = {'Authorization': f'Bearer {self.token}'}
            request_api = await self.request_module.get(url=f'https://api.spotify.com/v1/artists/{artist_id}'
                                                            f'/related-artists',
                                                        headers=request_headers)
            if int(request_api.status_code) != 200:
                return {'error': True, 'code': int(request_api.status_code)}
            request_api = request_api.json()
        except:
            raise ValueError('The selected Spotify token is invalid, or an external error occurred on the server.')

        return request_api

    async def get_artist_albums(self, artist_id: str = None, offset: int = 0, limit: int = 20):
        if artist_id is None:
            raise AttributeError('This method requires the artist ID to be specified.')

        try:
            request_headers = {'Authorization': f'Bearer {self.token}'}
            request_api = await self.request_module.get(url=f'https://api.spotify.com/v1/artists/{artist_id}'
                                                            f'/albums?offset={offset}&limit={limit}',
                                                        headers=request_headers)
            if int(request_api.status_code) != 200:
                return {'error': True, 'code': int(request_api.status_code)}
            request_api = request_api.json()
        except:
            raise ValueError('The selected Spotify token is invalid, or an external error occurred on the server.')

        return request_api

    async def get_user_following(self, sort_type: str = 'artist', limit: int = 20):
        try:
            request_headers = {'Authorization': f'Bearer {self.token}'}
            request_api = await self.request_module.get(url='https://api.spotify.com/v1/me/following'
                                                            f'?limit={limit}&type={sort_type}',
                                                        headers=request_headers)
            if int(request_api.status_code) != 200:
                return {'error': True, 'code': int(request_api.status_code)}
            request_api = request_api.json()
        except:
            raise ValueError('The selected Spotify token is invalid, or an external error occurred on the server.')

        return request_api

    async def get_user_top(self, sort_type: str = 'artists', time_range: str = 'medium_term',
                           limit: int = 20, offset: int = 0):
        try:
            request_headers = {'Authorization': f'Bearer {self.token}'}
            request_api = await self.request_module.get(url=f'https://api.spotify.com/v1/me/top/{sort_type}'
                                                            f'?time_range={time_range}&limit={limit}&offset={offset}',
                                                        headers=request_headers)
            if int(request_api.status_code) != 200:
                return {'error': True, 'code': int(request_api.status_code)}
            request_api = request_api.json()
        except:
            raise ValueError('The selected Spotify token is invalid, or an external error occurred on the server.')

        return request_api

    async def get_user_recent(self, limit: int = 20):
        try:
            request_headers = {'Authorization': f'Bearer {self.token}'}
            request_api = await self.request_module.get(url=f'https://api.spotify.com/v1/me/player/recently-played'
                                                            f'?limit={limit}',
                                                        headers=request_headers)
            if int(request_api.status_code) != 200:
                return {'error': True, 'code': int(request_api.status_code)}
            request_api = request_api.json()
        except:
            raise ValueError('The selected Spotify token is invalid, or an external error occurred on the server.')

        return request_api

    async def get_user_devices(self):
        try:
            request_headers = {'Authorization': f'Bearer {self.token}'}
            request_api = await self.request_module.get(url=f'https://api.spotify.com/v1/me/player/devices',
                                                        headers=request_headers)
            if int(request_api.status_code) != 200:
                return {'error': True, 'code': int(request_api.status_code)}
            request_api = request_api.json()
        except:
            raise ValueError('The selected Spotify token is invalid, or an external error occurred on the server.')

        return request_api

    async def get_user_playlists(self, user_id: str = None, offset: int = 0, limit: int = 20):
        if user_id is None:
            raise AttributeError('This method requires the user ID to be specified.')
        try:
            request_headers = {'Authorization': f'Bearer {self.token}'}
            request_api = await self.request_module.get(url=f'https://api.spotify.com/v1/users/{user_id}/playlists'
                                                            f'?offset={offset}&limit={limit}',
                                                        headers=request_headers)
            if int(request_api.status_code) != 200:
                return {'error': True, 'code': int(request_api.status_code)}
            request_api = request_api.json()
        except:
            raise ValueError('The selected Spotify token is invalid, or an external error occurred on the server.')

        return request_api

    async def search_item(self, query: str = None, search_type: str = 'track', limit: int = 20, offset: int = 0):
        if query is None or search_type is None:
            raise AttributeError('This method requires the query/search_type to be specified.')
        try:
            request_headers = {'Authorization': f'Bearer {self.token}'}
            request_api = await self.request_module.get(url=f'https://api.spotify.com/v1/search?q={query}'
                                                            f'&limit={limit}&offset={offset}',
                                                        headers=request_headers)
            if int(request_api.status_code) != 200:
                return {'error': True, 'code': int(request_api.status_code)}
            request_api = request_api.json()
        except:
            raise ValueError('The selected Spotify token is invalid, or an external error occurred on the server.')

        return request_api

    async def get_user(self, user_id: str = None):
        if user_id is None:
            raise AttributeError('This method requires the user ID to be specified.')
        try:
            request_headers = {'Authorization': f'Bearer {self.token}'}
            request_api = await self.request_module.get(url=f'https://api.spotify.com/v1/users/{user_id}',
                                                        headers=request_headers)
            if int(request_api.status_code) != 200:
                return {'error': True, 'code': int(request_api.status_code)}
            request_api = request_api.json()
        except:
            raise ValueError('The selected Spotify token is invalid, or an external error occurred on the server.')

        return request_api

    async def get_track(self, track_id: str = None):
        if track_id is None:
            raise AttributeError('This method requires the track ID to be specified.')
        try:
            request_headers = {'Authorization': f'Bearer {self.token}'}
            request_api = await self.request_module.get(url=f'https://api.spotify.com/v1/tracks/{track_id}',
                                                        headers=request_headers)
            if int(request_api.status_code) != 200:
                return {'error': True, 'code': int(request_api.status_code)}
            request_api = request_api.json()
        except:
            raise ValueError('The selected Spotify token is invalid, or an external error occurred on the server.')

        return request_api
