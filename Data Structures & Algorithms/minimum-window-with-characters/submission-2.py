class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ct = {}
        for c in t:
            ct[c] = ct.get(c,0) + 1
        
        ans = ""
        l,r = 0,0
        cs = {}
        match = 0
        target = len(ct.keys())
        while r < len(s):
            cs[s[r]] = cs.get(s[r],0) + 1
            if s[r] in ct and cs[s[r]] == ct[s[r]]:
                match += 1
            
            while match == target:
                cs[s[l]] -= 1
                if s[l] in ct and cs[s[l]] == ct[s[l]] - 1:
                    match -= 1
                if ans == "" or r - l + 1 < len(ans):
                    ans = s[l:r + 1]
                l += 1

            r += 1
        return ans
            