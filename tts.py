#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-07-29 22:24:28

import begin
from gtts import gTTS

def say(text, fname):
    tts = gTTS(text)
    tts.save(fname)

@begin.start
def main(arg1 = None):
    fname = 'tts.mp3'
    tts = gTTS('this is a test; a, rather long test; of text 2 speach', lang='en', tld='ca')
    tts.save(fname)
