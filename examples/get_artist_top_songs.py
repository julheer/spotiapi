# -*- coding: utf-8 -*-
from asyncio import run

from spotiapi import SpotifyAPIWrapper

spotify = SpotifyAPIWrapper('spotify_api_token')


async def request_data():
    artist = input()
    request_songs = await spotify.get_artist_top_songs(artist)
    if 'error' in request_songs:
        return print(f'Something went wrong... ({request_songs["code"]})')

    return print(f'Received data: {request_songs}')


if __name__ == '__main__':
    run(request_data())
