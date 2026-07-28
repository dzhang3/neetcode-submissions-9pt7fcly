class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        nf = {}
        for s in s1:
            nf[s] = nf.get(s,0) + 1
        
        eq = 0
        distinct = len(nf.keys())
        mf = {}
        for s in s2[:n]:
            mf[s] = mf.get(s,0) + 1
            if s in nf and mf[s] == nf[s]:
                eq += 1
            elif s in nf and mf[s] == nf[s] + 1:
                eq -= 1

        for i in range(m - n + 1):
            # print(eq,distinct)
            if eq == distinct:
                return True
            if i == m - n:
                break
            
            s = s2[i + n]
            mf[s] = mf.get(s,0) + 1
            if s in nf and mf[s] == nf[s]:
                eq += 1
            elif s in nf and mf[s] == nf[s] + 1:
                eq -= 1
            
            s = s2[i]
            mf[s] -= 1
            if s in nf and mf[s] == nf[s]:
                eq += 1
            elif s in nf and mf[s] == nf[s] - 1:
                eq -= 1
            
        return False