class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 0
        # create edges
        nb = defaultdict(list)
        def isNeighbor(w1,w2):
            diff = False
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    if diff:
                        return False
                    diff = True
            return True
        wordList.append(beginWord)
        for i in range(len(wordList)):
            for j in range(i):
                if isNeighbor(wordList[i],wordList[j]):
                    nb[wordList[i]].append(wordList[j])
                    nb[wordList[j]].append(wordList[i])
        if endWord not in nb.keys():
            return 0
        
        #bfs
        queue = deque()
        queue.append(beginWord)
        visited = set()

        ans = 0
        while queue:
            newQueue = deque()
            while queue:
                w = queue.popleft()
                if w == endWord:
                    return ans + 1
                visited.add(w)
                for n in nb[w]:
                    if n not in visited:
                        newQueue.append(n)
            ans += 1
            queue = newQueue
        return 0