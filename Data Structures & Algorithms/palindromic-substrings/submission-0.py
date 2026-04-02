class Solution:
    def countSubstrings(self, s: str) -> int:
        def getPalin(s,i1, i2):
            count = 0
            while i1 >= 0 and i2 < len(s) and s[i1] == s[i2]:
                count += 1
                i1 -= 1
                i2 += 1
            return count
        count = 0
        for i in range(len(s)):
            count += getPalin(s,i,i)
            count += getPalin(s,i,i + 1)
        return count


        
