class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {0: True, len(s): False}
        for i in range(len(s)):
            for word in wordDict:
                start = i - len(word) + 1
                if dp.get(start,False):
                    substr = s[start:i + 1]
                    if word == substr:
                        dp[i + 1] = True
        return dp[len(s)]

        