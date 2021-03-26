from requests import get

class SpotifyAPI:
	def __init__(self, client_token):
		self.token = client_token

	def getUserCurrentTrack(self):
		request_headers = {'Authorization': f'Bearer {self.token}'}
		request_api = get(url='https://api.spotify.com/v1/me/player/currently-playing', headers=request_headers).json()

		try:
			song_artists = []
			for artist in request_api['item']['artists']:
				song_artists.append(artist['name'])
		except:
			raise ValueError('The selected Spotify token is invalid, or an external error occurred on the server.')

		return song_artists, request_api['item']['name']


	def getUserLikedAlbums(self):
		request_headers = {'Authorization': f'Bearer {self.token}'}
		request_api = get(url='https://api.spotify.com/v1/me/albums', headers=request_headers).json()

		try:
			liked_albums = []
			for album_data in request_api['items']:
				if album_data['album']['album_type'] != 'album':
					continue
				else:
					liked_albums.append({album_data['album']['name']: album_data['album']})
		except:
			raise ValueError('The selected Spotify token is invalid, or an external error occurred on the server.')

		return liked_albums


	def getUserPlaylists(self):
		request_headers = {'Authorization': f'Bearer {self.token}'}
		request_api = get(url='https://api.spotify.com/v1/me/playlists', headers=request_headers).json()

		try:
			user_playlists = []
			for playlist in request_api['items']:
				user_playlists.append({playlist['id']: playlist['name']})
		except:
			raise ValueError('The selected Spotify token is invalid, or an external error occurred on the server.')

		return user_playlists


	def getUserData(self):
		try:
			request_headers = {'Authorization': f'Bearer {self.token}'}
			request_api = get(url='https://api.spotify.com/v1/me', headers=request_headers).json()
		except:
			raise ValueError('The selected Spotify token is invalid, or an external error occurred on the server.')
			
		return request_api
