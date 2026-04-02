class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        actions = [(1,1),(1,0),(0,1)]
        def dfs(i,j):
            if i == len(word1) and j == len(word2):
                return 0
            elif i == len(word1): 
                return dfs(i,j + 1) + 1 # insert 
            elif j == len(word2):
                return dfs(i + 1,j) + 1 # delete
            elif word1[i] != word2[j]:
                ops = []
                if i < (len(word1)) and (j < len(word2)):
                    ops.append(dfs(i+1,j+1)) # replace
                if i < (len(word1)):
                    ops.append(dfs(i + 1,j)) # delete
                if j < (len(word2)):
                    ops.append(dfs(i,j + 1)) # insert 
                return min(ops) + 1
            else:
                return dfs(i+1,j+1)
        return dfs(0,0)
        
            