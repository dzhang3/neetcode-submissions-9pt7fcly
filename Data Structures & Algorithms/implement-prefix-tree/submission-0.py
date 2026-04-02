class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if not cur.children[ord(c) - ord('a')]:
                cur.children[ord(c) - ord('a')] = TrieNode()
            cur = cur.children[ord(c) - ord('a')]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if not cur.children[ord(c) - ord('a')]:
                return False
            cur = cur.children[ord(c) - ord('a')]
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if not cur.children[ord(c) - ord('a')]:
                return False
            cur = cur.children[ord(c) - ord('a')]
        return True
        