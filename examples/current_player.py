from spotiapi import SpotifyAPI
spotify = SpotifyAPI('spotify_token')

request_track = spotify.getUserCurrentTrack()
print(f'Listening now {request_track[1]}')
