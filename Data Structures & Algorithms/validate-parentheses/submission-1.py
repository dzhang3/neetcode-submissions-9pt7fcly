class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')':'(', '}':'{',']':'['}
        for c in s:
            if c in pairs:
                if not stack:
                    return False
                o = stack.pop()
                if o != pairs[c]:
                    return False
            else:
                stack.append(c)
        return not stack