class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        return [v for k,v in sorted([(v,k) for k,v in c.items()],reverse=True)[:k]]