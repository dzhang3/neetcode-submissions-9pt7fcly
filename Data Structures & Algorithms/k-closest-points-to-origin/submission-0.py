class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for (x,y) in points:
            dist = x**2 + y**2
            heap.append((dist,x,y))
        heapq.heapify(heap)
        
        ans = []
        for _ in range(k):
            dist,x,y = heapq.heappop(heap)
            ans.append([x,y])
        return ans