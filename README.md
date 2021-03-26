# spotiapi
A small library for getting convenient and structured information about the Spotify user (currently only about the user who created the app key).
Last library version - **1.0.1 (release 26.03)**. 

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
from spotiapi import SpotifyAPI
spotify = SpotifyAPI('spotify_token')

print(spotify.getUserData())
```

You can find other examples [here](https://github.com/julheer/spotiapi/blob/main/examples), or on the pages of other users who used this repository and pointed this repository out.

## Todos & plans:
- [ ] Add unit tests.
- [ ] Add descriptions for functions in the code.
- [X] Fix the error with the names in the `getUserLikedAlbums` and `getUserPlaylists` functions.
- [ ] Conduct final testing.
- [ ] Release the latest DEV version (**1.1**).

© [Julheer](https://github.com/julheer), 2021. Developed with ❤.
