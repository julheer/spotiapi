from asyncio import run

from spotiapi import SpotifyAPIWrapper

wrapper = SpotifyAPIWrapper('')

print(run(wrapper.get_player()))
