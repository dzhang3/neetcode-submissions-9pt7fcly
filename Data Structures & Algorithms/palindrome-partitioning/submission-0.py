class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def isPalindrome(s):
            if not s:
                return False
            l,r = 0,len(s) - 1
            while l <= r and s[l] == s[r]:
                l += 1
                r -= 1
            return l > r

        def dfs(t,i,l):
            if isPalindrome(t):
                l.append(t)
                if i == len(s): 
                    ans.append(l.copy())
                    l.pop()
                    return
                dfs(s[i], i + 1,l)
                l.pop()
            if i == len(s):
                return
            dfs(t + s[i], i + 1,l)
        dfs("",0,[])
        return ans
