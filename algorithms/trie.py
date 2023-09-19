#!/usr/bin/env python3
# dpw@plaza.localdomain
# 2023-09-19 17:28:16

import sys
from rich import print, inspect
from dataclasses import dataclass

class TrieNode:
    def __init__(self):
        self.children = [None] * 26

        self.word_count = 0

    def __repr__(self):
        clist = [child for child in self.children if child is not None]
        return f"word_count: {self.word_count}, children: {clist}"

@dataclass
class TrieContainer:
    root = TrieNode()

    def normalize(self, key: str) -> str:
        word = []
        for ch in key.lower():
            idx = ord(ch) - ord('a')
            if idx in range(26):
                word.append(ch)

        return word

    def insert(self, key: str) -> None:
        key = self.normalize(key)
        current = self.root

        for ch in key:
            idx = ord(ch) - ord('a')
            if current.children[idx] is None:
                new_node = TrieNode()
                current.children[idx] = new_node

            current = current.children[idx]

        current.word_count += 1

    def exists(self, key: str) -> bool:
        key = self.normalize(key)
        current = self.root

        for ch in key:
            idx = ord(ch) - ord('a')
            if current.children[idx] is None:
                return False

            current = current.children[idx]

        return True

    def search(self, key: str) -> int:
        key = self.normalize(key)
        current = self.root

        for ch in key:
            idx = ord(ch) - ord('a')
            if current.children[idx] is None:
                return False

            current = current.children[idx]

        return current.word_count > 0

    def remove(self, key: str):
        pass


def main(args: list) -> None:
    print(f'{args}')
    trie = TrieContainer()
    trie.insert('and')

    inspect(trie.root)

    print(f"exists: {trie.exists('and')}")
    print(f"search: {trie.search('and')}")

if __name__ == '__main__':
    main(sys.argv[1:])

