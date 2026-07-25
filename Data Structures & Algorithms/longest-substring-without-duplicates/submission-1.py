class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = defaultdict(int)
        l,r = 0,0
        ans = 0
        while r < len(s):
            count[s[r]] += 1
            while count[s[r]] > 1:
                count[s[l]] -= 1
                l += 1
            ans = max(ans,r - l + 1)
            r += 1
        return ans

        
        