class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        status = [0] * numCourses
        nb = defaultdict(list)
        for c1, c2 in prerequisites:
            nb[c1].append(c2)
        ans = []
        def dfs(c):
            nonlocal ans
            if status[c] == 1:
                return False
            if status[c] == 2:
                return True
            
            status[c] = 1
            for n in nb[c]:
                if not dfs(n):
                    return False
            status[c] = 2
            ans.append(c)
            return True
        
        for i in range(numCourses):
            if status[i] == 0:
                if not dfs(i):
                    return []
        
        return ans
        

