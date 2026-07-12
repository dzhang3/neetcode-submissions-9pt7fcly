class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        freqs = defaultdict(list)
        for j,v in c.items():
            freqs[v].append(j)
        
        ans = []
        for i in range(len(nums),-1,-1):
            if k == 0:
                return ans
            # print(freqs[i],k)
            ans = ans + freqs[i]
            k -= len(freqs[i])
        return ans
            