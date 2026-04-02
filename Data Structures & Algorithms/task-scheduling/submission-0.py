class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = {}
        for t in tasks:
            freqs[t] = freqs.get(t,0) + 1
        
        heap = []
        for t,x in freqs.items():
            heap.append((x,t))
        heapq.heapify_max(heap)

        interval = 0
        prevs = {}
        while heap:
            f,i = heapq.heappop_max(heap)
            addback = []
            while len(heap) > 0 and (i in prevs) and (interval - prevs[i] <= n):
                addback.append((f,i))
                f,i = heapq.heappop_max(heap)
            if i not in prevs or interval - prevs[i] > n:
                prevs[i] = interval
                if f > 1: addback.append((f-1,i))
            else:
                addback.append((f,i))
            for item in addback:
                heapq.heappush_max(heap,item)
            interval += 1
        return interval
