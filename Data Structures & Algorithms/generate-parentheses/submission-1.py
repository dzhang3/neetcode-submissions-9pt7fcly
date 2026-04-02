class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def parens(o,c,s):
            if o == c == n:
                ans.append(s)
                return
            if o > n or c > n or c > o:
                return
            parens(o+1,c,s + "(")
            parens(o,c + 1,s + ")")
        parens(0,0,"")
        return ans