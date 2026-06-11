class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # dijkstra's algo
        nb = defaultdict(list)
        for ui,vi,ti in times:
            nb[ui].append((vi,ti))
        
        times = [-1] * (n + 1)
        times[k] = 0
         
        heap = []
        heapq.heappush(heap,(0,k))

        while heap:
            t,u = heapq.heappop(heap)
            
            if times[u] != -1 and t > times[u]:
                continue
            
            for v,tv in nb[u]:
                if times[v] == -1 or t + tv < times[v]:
                    times[v] = t + tv
                    heapq.heappush(heap,(t + tv,v))

        
        if -1 in times[1:]:
            return -1
        
        return max(times)