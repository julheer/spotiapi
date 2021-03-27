from spotiapi import SpotifyAPI
spotify = SpotifyAPI('spotify_api_token')

request_player = spotify.get_user_player()
if request_player[0]:
	print(f'Now playing {request_player[2]} by {request_player[1]}')
	# -> Now playing SONG_NAME by ARTIST(S)
