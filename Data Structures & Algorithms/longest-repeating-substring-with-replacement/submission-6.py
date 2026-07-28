class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0
        freqs = defaultdict(int)
        ans = 0
        while r < len(s):
            freqs[s[r]] += 1
            while max(freqs.values()) + k < r - l + 1:
                freqs[s[l]] -= 1
                l += 1
            ans = max(ans,r - l + 1)
            r += 1
        return ans