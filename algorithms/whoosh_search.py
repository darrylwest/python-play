#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-19 23:21:55

import sys
from rich import print, inspect
from dataclasses import dataclass
from whoosh.index import create_in, open_dir
from whoosh.fields import *
from whoosh.qparser import QueryParser

# class MySchema(SchemaClass):

# The results does not match documentation.


@dataclass
class SearchEngine:
    index_dir = "indexdir"
    schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)
    # ix = create_in(index_dir, schema)
    ix = open_dir(index_dir)

    def index(self):
        ix = self.ix
        writer = ix.writer()
        writer.add_document(
            title="First document",
            path="/a",
            content="This ithe first document we've added",
        )
        writer.add_document(
            title="Second document",
            path="/u",
            content="The second document even better!",
        )
        writer.commit()

    def search(self, word):
        ix = self.ix
        with ix.searcher() as searcher:
            query = QueryParser("content", ix.schema).parse(word)
            results = searcher.search(query)

        return results


engine = SearchEngine()


def main(args: list) -> None:
    # print(f'{args}')

    # engine.index()
    result = engine.search("first")

    inspect(result)


if __name__ == "__main__":
    main(sys.argv[1:])
