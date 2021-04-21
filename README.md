# spotiapi
A small library for getting convenient and structured information about the Spotify user (currently only about the user who created the app key).
Last library version - **1.2.5 (release 09.04)**.

![MIT](https://img.shields.io/github/license/Julheer/spotiapi.svg)
![Version](https://img.shields.io/pypi/v/spotiapi)

## Requirements
This library requires one additional library: [requests](https://github.com/psf/requests) (versions **2.25.1 and higher**).
It will be installed automatically when you download my library from PyPI.

## Installation
To install the library, you will need the Python - `pip` package manager. You can install the library by writing a single command - `pip install -U spotiapi`. You can also specify a specific version. Please [check this](https://pypi.org/project/spotiapi) for more information.

## Examples
Getting information about the user who created the current token:
```python
from asyncio import run
from spotiapi import SpotifyAPIWrapper

spotify = SpotifyAPIWrapper('spotify_api_token')


async def request_data():
    request_self = await spotify.get_self()
    if 'error' in request_self:
        return print(f'Something went wrong... ({request_self["code"]})')

    return print(f'Hello, {request_self["display_name"]}!')

if __name__ == '__main__':
    run(request_data())

```

You can find other examples [here](https://github.com/julheer/spotiapi/blob/main/examples), or on the pages of other users who used this repository and pointed this repository out.

© [Julheer](https://github.com/julheer), 2021. Developed with ❤.
