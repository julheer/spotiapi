from spotiapi import SpotifyAPI
spotify = SpotifyAPI('spotify_token')

request_user = spotify.getUserData()
print(f'Hello, {request_user["display_name"]}! You have {request_user["followers"]["total"]} subs.')
