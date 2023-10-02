#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-19 19:17:00

import json
import sys
from dataclasses import dataclass
from pathlib import Path

from rich import inspect, print


class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {}

    def __repr__(self):
        return f"char:{self.char}, end: {self.is_end}, children: {self.children}"


@dataclass
class Trie:
    """A container for holding Trie nodes.  Will store and word, name, email, phone number, etc."""

    root: TrieNode = TrieNode("")
    word_count: int = 0

    def insert(self, word: str) -> None:
        word = word.lower()
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        node.is_end = True
        self.word_count += 1

    def depth_first_search(self, node: TrieNode, prefix: str):
        """depth first search"""
        if node.is_end:
            self.output.append((prefix + node.char))

        for child in node.children.values():
            self.depth_first_search(child, prefix + node.char)

    def search(self, word: str) -> list:
        """search for words"""
        word = word.lower()
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return []

        self.output = []
        self.depth_first_search(node, word[:-1])

        return self.output


def read_proper_names() -> Trie:
    trie = Trie()
    path = Path("/usr/share/dict/propernames")
    for name in path.read_text().split():
        trie.insert(name)

    return trie


def read_data():
    with open("data/emails.json") as f:
        data = json.load(f)

    return data


def insert_data(trie: Trie, data):
    for v in data:
        trie.insert(v)


trie = Trie()
data = read_data()


def main(args: list) -> None:
    # print(f'{args}')

    insert_data(trie, data)


if __name__ == "__main__":
    main(sys.argv[1:])
