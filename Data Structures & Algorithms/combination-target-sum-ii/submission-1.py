class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        res = []
        def dfs(i,cursum, subset):
            if cursum == target:
                res.append(subset.copy())
            if i == len(candidates) or cursum >= target:
                return
            dfs(i+1,cursum + candidates[i],subset + [candidates[i]])
            while i < len(candidates) - 1 and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1,cursum,subset)
        dfs(0,0,[])
        return res