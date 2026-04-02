class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            num = (1 << i)
            if num & n: count += 1
        return count