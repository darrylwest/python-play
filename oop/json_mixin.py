#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-18 16:37:54

import json

class JsonMixin:
    def to_json(self):
        return json.dumps(self.__dict__)


