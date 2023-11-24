#!/usr/bin/env python3.12
# dpw@plaza.local
# 2023-11-24 19:09:14

import sys
from rich import inspect
import flickrapi
import webbrowser
import auth

# todo put in .env
# user_id = u'84667439@N00'
# api_key = u'd4c52b961a95af1794ce5c1fa771523f'
# api_secret = u'2e3e15f4d571312d'

def main() -> None:
    api_key = auth.get_api_key()
    api_secret = auth.get_secret()
    user_id = auth.get_user_id()

    print(api_key, api_secret, user_id)

    flickr = flickrapi.FlickrAPI(api_key, api_secret)

    photos = flickr.photos.search(user_id=user_id, per_page=10, format='parsed-json')
    inspect(photos)
    print(photos)

if __name__ == '__main__':
    main()
