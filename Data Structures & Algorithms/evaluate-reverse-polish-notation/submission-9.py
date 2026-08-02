class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numstack = []
        for t in tokens:
            if t == '+':
                numstack.append(
                    (numstack.pop()) + (numstack.pop())
                )
            elif t == '*':
                numstack.append(
                    (numstack.pop()) * (numstack.pop())
                )
            elif t == '/':
                b = (numstack.pop())
                a = (numstack.pop())
                numstack.append(
                    int(float(a) / (b))
                )
            elif t == '-':
                b,a = numstack.pop(),numstack.pop()
                numstack.append(
                    int(a) - int(b)
                )
            else:
                numstack.append(int(t))
        return (numstack[0])