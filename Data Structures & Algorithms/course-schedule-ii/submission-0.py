class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = defaultdict(list)
        for c,p in prerequisites:
            prereqs[c].append(p)
        
        states = [-1] * numCourses
        ans = []
        def dfs(num):
            if states[num] == 0:
                return False
            if states[num] == 1:
                return True
            states[num] = 0
            for pre in prereqs[num]:
                if not dfs(pre):
                    return False
            states[num] = 1
            ans.append(num)
            return True
        
        for i in range(numCourses):
            if states[i] == -1:
                if not dfs(i):
                    return []
        return ans

        