class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1c = {}
        for s in s1:
            s1c[s] = s1c.get(s,0) + 1
        
        l,r = 0,0
        s2c = {}
        while r < len(s2):
            s = s2[r]
            s2c[s] = s2c.get(s,0) + 1
            while s2c[s] > s1c.get(s,0) and l <= r:
                s2c[s2[l]] -= 1
                l += 1
            
            if r - l + 1 == len(s1):
                return True
            r += 1
        return False

        