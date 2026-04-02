class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        l,r = 0,0
        freqs = [0] * 26
        maxChar = 0
        while r < len(s):
            freqs[ord(s[r]) - ord('A')] += 1
            maxChar = max(maxChar, freqs[ord(s[r]) - ord('A')])
            if l < r and r - l  + 1 > maxChar + k:
                freqs[ord(s[l]) - ord('A')] -= 1
                # maxChar = max(freqs)
                l += 1
            maxLen = max(maxLen, r - l + 1)
            r += 1
        return maxLen
            