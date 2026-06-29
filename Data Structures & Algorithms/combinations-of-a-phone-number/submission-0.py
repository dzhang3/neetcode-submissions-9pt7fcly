class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        letters = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }

        ans = []

        def dfs(s,i):
            if i >= len(digits):
                ans.append(s)
                return
            # print(i,len(digits))
            for l in letters[digits[i]]:
                dfs(s + l,i + 1)
        
        dfs('',0)
        return ans
            