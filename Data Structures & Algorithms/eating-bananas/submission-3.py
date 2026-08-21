class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours(k):
            hrs = 0
            for p in piles:
                hrs += math.ceil(p / k)
            print(hrs)
            return hrs <= h

        l,r = 1,max(piles)
        ans = r
        while l <= r:
            m = (l + r) // 2
            # print(m,hours(m))
            if hours(m):
                ans = m
                r = m - 1
            else:
                l = m + 1
        return ans
