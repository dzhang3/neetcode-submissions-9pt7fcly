class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(list)
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        for i in count.keys():
            freqs[count[i]].append(i)
        ans = []
        for i in range(len(nums),0,-1):
            for n in freqs[i]:
                if k == 0:
                    return ans
                ans.append(n)
                k -= 1
        return ans
            

        