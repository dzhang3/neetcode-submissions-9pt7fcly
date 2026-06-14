class Solution:
    def checkValidString(self, s: str) -> bool:
        opens = []
        stars = []
        for i,c in enumerate(s):
            if c == '*':
                stars.append(i)
            elif c == ')':
                if not opens and not stars:
                    return False
                elif opens:
                    opens.pop()
                elif stars:
                    stars.pop()
            elif c == '(':
                opens.append(i)

        while opens and stars:
            oi,si = opens.pop(),stars.pop()
            if si < oi:
                return False
        return not opens