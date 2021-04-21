# -*- coding: utf-8 -*-
from asyncio import run

from spotiapi import SpotifyAPIWrapper

spotify = SpotifyAPIWrapper('spotify_api_token')


async def request_data():
    request_player = await spotify.get_player()
    if 'error' in request_player:
        return print(f'Something went wrong... ({request_player["code"]})')
    elif request_player['is_playing']:
        return print(f'Now playing {request_player["player_name"]} by {request_player["player_artists"]}')
        # -> Now playing SONG_NAME by ARTIST(S)


if __name__ == '__main__':
    run(request_data())
