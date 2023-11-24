#!/usr/bin/env python3.11
# dpw@9ba12012843f
# 2023-11-24 18:33:15

import sys
from rich import inspect
import flickrapi
import webbrowser

user_id = u'84667439@N00'
api_key = u'd4c52b961a95af1794ce5c1fa771523f'
api_secret = u'2e3e15f4d571312d'

def main() -> None:
    flickr = flickrapi.FlickrAPI(api_key, api_secret)
    if not flickr.token_valid(perms='read'):
        flickr.get_request_token(oauth_callback='oob')

        authorize_url = flickr.auth_url(perms='read')
        webbrowser.open_new_tab(authorize_url)

        verifier = str(input('Verifier code: '))

        flickr.get_access_token(verifier)

    resp = flickr.photos.getInfo(photo_id='52656157977')
    inspect(resp)


if __name__ == '__main__':
    main()
