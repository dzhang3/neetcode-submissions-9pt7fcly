class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        l,r = 0,0
        lastInd = {}
        for i,c in enumerate(s):
            lastInd[c] = i
        # lastInd = {x: 3, y: 4, z: 7, b: 9}
        
        ans = []
        while r < len(s):
            end = lastInd[s[l]]
            while r <= end:
                end = max(end,lastInd[s[r]])
                r += 1
            ans.append(r - l)
            l = r
        return ans
            