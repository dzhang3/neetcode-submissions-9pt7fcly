class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ans = []
        indegrees = [0] * numCourses
        neighbors = defaultdict(list)
        for c1, c2 in prerequisites:
            indegrees[c1] += 1
            neighbors[c2].append(c1)
        
        queue = deque()
        for c,ind in enumerate(indegrees):
            if ind == 0:
                queue.append(c)
        while queue:
            c = queue.popleft()
            ans.append(c)
            for n in neighbors[c]:
                indegrees[n] -= 1
                if indegrees[n] == 0:
                    queue.append(n)

        return len(ans) == numCourses
