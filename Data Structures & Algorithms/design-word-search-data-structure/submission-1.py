class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if not cur.children[ord(c) - ord('a')]:
                cur.children[ord(c) - ord('a')] = TrieNode()
            cur = cur.children[ord(c) - ord('a')]
        cur.isEnd = True        
        

    def search(self, word: str) -> bool:
        stack = [(self.root,0)]
        
        while stack:
            cur,ind = stack.pop()
            if ind == (len(word)) and cur.isEnd:
                return True
            if ind < len(word):
                if word[ind] == '.':
                    for child in cur.children:
                        if child:
                            stack.append((child,ind + 1))
                else:
                    if cur.children[ord(word[ind]) - ord('a')]:
                        stack.append((cur.children[ord(word[ind]) - ord('a')],ind + 1))
        return False
                
