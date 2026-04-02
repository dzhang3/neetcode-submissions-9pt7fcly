class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = Counter(tasks)
        heap = list(freqs.values())
        heapq.heapify_max(heap)
        
        time = 0
        cooldown = deque() # (freq,cooldowntime)
        while heap or cooldown:
            time += 1
            if not heap:
                time = cooldown[0][1]
            else:
                count = heapq.heappop_max(heap) - 1
                if count:
                    cooldown.append((count,time + n))
            if cooldown and cooldown[0][1] == time:
                heapq.heappush_max(heap,cooldown.popleft()[0])
        return time
