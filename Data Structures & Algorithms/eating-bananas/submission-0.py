import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l <= r:
            k = (l + r) // 2
            th = 0
            works = True
            for p in piles:
                th += math.ceil(p / k)
                if th > h:
                    works = False
            
            if (works):
                r = k - 1
            else:
                l = k + 1
        return l