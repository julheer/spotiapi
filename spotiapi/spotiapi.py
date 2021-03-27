from requests import get


class SpotifyAPI:
    def __init__(self, client_token):
        self.token = client_token

    @property
    def get_package_version(self):
        with open('../version.txt') as version:
            return version.read()

    @property
    def get_user_player(self):
        """
        This function returns the current track and the artist that the user is currently listening to.
        If the user is not listening to anything, the last track they listened to will be returned.
        """
        request_headers = {'Authorization': f'Bearer {self.token}'}
        request_api = get(url='https://api.spotify.com/v1/me/player/currently-playing', headers=request_headers).json()

        try:
            is_playing = False
            if request_api['is_playing']:
                is_playing = True

            song_artists = []
            for artist in request_api['item']['artists']:
                song_artists.append(artist['name'])
        except:
            raise ValueError('The selected Spotify token is invalid, or an external error occurred on the server.')

        return is_playing, song_artists, request_api['item']['name']

    @property
    def get_liked_albums(self):
        """
        The function returns all the albums that the user added to liked, or None if no albums were added.
        """
        request_headers = {'Authorization': f'Bearer {self.token}'}
        request_api = get(url='https://api.spotify.com/v1/me/albums', headers=request_headers).json()

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

    @property
    def get_playlists(self):
        """
        This function returns a list of playlists that the user has created or added to important ones.
        """
        request_headers = {'Authorization': f'Bearer {self.token}'}
        request_api = get(url='https://api.spotify.com/v1/me/playlists', headers=request_headers).json()

        try:
            user_playlists = []

            if 'items' not in request_api:
                user_playlists = None

            for playlist in request_api['items']:
                user_playlists.append({'name': playlist['name'], 'id': playlist['id']})
        except:
            raise ValueError('The selected Spotify token is invalid, or an external error occurred on the server.')

        return user_playlists

    @property
    def get_self_user(self):
        """
        This function returns a user data object.
        """
        try:
            request_headers = {'Authorization': f'Bearer {self.token}'}
            request_api = get(url='https://api.spotify.com/v1/me', headers=request_headers).json()
        except:
            raise ValueError('The selected Spotify token is invalid, or an external error occurred on the server.')

        return request_api
