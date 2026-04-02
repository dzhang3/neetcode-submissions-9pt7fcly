class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def lmao(o,c):
            if o == c == n:
                res.append("".join(stack))
            
            if o < n:
                stack.append('(')
                lmao(o+1,c)
                stack.pop()
            if c < o:
                stack.append(')')
                lmao(o,c + 1)
                stack.pop()
        
        lmao(0,0)
        return res