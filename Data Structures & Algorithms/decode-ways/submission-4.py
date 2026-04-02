class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        dp = [1] * (len(s) + 1)
        for i,c in enumerate(s):
            if i == 0:
                continue
            if c == '0':
                if int(s[i-1]) > 2 or int(s[i-1]) == 0:
                    return 0
                else:
                    dp[i+1] = dp[i] = dp[i-1]
                continue
            canApp = True if s[i-1] != '0' and int(s[i-1] + c) <= 26 and int(s[i-1] + c) > 0 else False
            print(canApp,s[i],int(s[i] + c))
            p1 = dp[i]
            p2 = dp[i-1] if canApp else 0
            dp[i+1] = p1 + p2
        print(dp)
        return dp[-1]
            