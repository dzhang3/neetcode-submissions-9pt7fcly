class Solution:
    def longestPalindrome(self, s: str) -> str:
        def getPalin(s,i1, i2):
            while i1 >= 0 and i2 < len(s) and s[i1] == s[i2]:
                i1 -= 1
                i2 += 1
            return s[i1+1:i2]

        longest = 0
        ans = ""
        for i in range(len(s)):
            p1 = getPalin(s,i,i)
            p2 = ''
            if i + 1 < len(s):
                p2 = getPalin(s,i,i + 1)
            if max(len(p1),len(p2)) > longest:
                if len(p1) > len(p2):
                    ans = p1
                    longest = len(p1)
                else:
                    ans = p2
                    longest = len(p2)
        return ans
