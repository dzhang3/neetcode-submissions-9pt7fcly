class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        tc = {}
        sc = {}
        for i in range(len(t)):
            tc[t[i]] = tc.get(t[i],0) + 1
            sc[s[i]] = sc.get(s[i],0) + 1
        
        matches = 0
        for x in tc.keys():
            if tc[x] <= sc.get(x,0):
                matches += 1

        target = len(tc.keys())

        l = 0
        res = ""
        if matches == target:
            res = s[:len(t)]

        for r in range(len(t), len(s)):

            sc[s[r]] = sc.get(s[r],0) + 1
            if sc[s[r]] == tc.get(s[r],0):
                matches += 1
            while matches == target and l <= r:
                if r - l + 1 < len(res) or len(res) == 0:
                    res = s[l:r + 1]
                sc[s[l]] -= 1
                if sc[s[l]] == tc.get(s[l],0) - 1:
                    matches -= 1
                l += 1

        return res


            
            

            
        
        