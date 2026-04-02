class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(list)
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        for i,n in count.items():
            freqs[n].append(i)
        ans = []
        for i in range(len(nums),0,-1):
            for n in freqs[i]:
                if k == 0:
                    return ans
                ans.append(n)
                k -= 1
        return ans
            

        