#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-07-29 22:24:28

from gtts import gTTS


def say(text, fname):
    tts = gTTS(text)
    tts.save(fname)


if __name__ == "__main__":
    fname = "tts.mp3"
    tts = gTTS(
        "this is a test; a, rather long test; of text 2 speach", lang="en", tld="ca"
    )
    tts.save(fname)
