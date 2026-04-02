class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        for _ in range(len(nums)):
            tmp = []
            for seq in ret:
                for num in nums:
                    if num not in seq:
                        tmp.append(seq + [num])

            ret = tmp
        return ret
