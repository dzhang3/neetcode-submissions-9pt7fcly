class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = [0] * 26
        maxFreq = 0
        l,r = 0,0
        res = 0

        while r < len(s):
            freqs[ord(s[r]) - ord('A')] += 1
            maxFreq = max(maxFreq, freqs[ord(s[r]) - ord('A')])

            while r - l + 1 > maxFreq + k:
                freqs[ord(s[l]) - ord('A')] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1 
        return res
        