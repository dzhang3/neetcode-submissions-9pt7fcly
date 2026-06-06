class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Kahns algorithm
        # get in degrees, add ones with 0

        indeg = [0] * numCourses
        nb = defaultdict(list)
        for c1, c2 in prerequisites:
            nb[c2].append(c1)
            indeg[c1] += 1
        
        queue = deque()
        for c,ind in enumerate(indeg):
            if ind == 0:
                queue.append(c)

        ans = []
        while queue:
            c = queue.popleft()
            ans.append(c)
            for n in nb[c]:
                indeg[n] -= 1
                if indeg[n] == 0:
                    queue.append(n)
        
        return ans if len(ans) == numCourses else []
        