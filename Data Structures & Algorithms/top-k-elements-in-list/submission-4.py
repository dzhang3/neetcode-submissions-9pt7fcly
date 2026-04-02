class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for n in nums:
            freqs[n] = freqs.get(n,0) + 1
        
        freqs = sorted(freqs.items(),key=lambda x: x[1],reverse=True)
        return [freq[0] for freq in freqs[:k]]