from dataclasses import dataclass, field
from typing import Self


@dataclass
class TrieNode:
    children: dict[str, Self] = field(init=False, default_factory=dict)
    visited: int = field(init=False, default=0)
    ended: int = field(init=False, default=0)


@dataclass
class Trie:
    root: TrieNode = field(init=False, default_factory=TrieNode)

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.visited += 1
        node.ended += 1

    def delete(self, word: str) -> None:
        node = self.root
        for c in word:
            node = node.children[c]
            node.visited -= 1
        node.ended -= 1

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.ended > 0

    def prefix(self, word: str) -> int:
        node = self.root
        for c in word:
            if c not in node.children:
                return 0
            node = node.children[c]
        return node.visited
