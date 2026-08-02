class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numstack = []
        for t in tokens:
            if t.isdigit() or (t[0] == '-' and len(t) > 1):
                numstack.append(t)
            elif t == '+':
                numstack.append(
                    int(numstack.pop()) + int(numstack.pop())
                )
            elif t == '*':
                numstack.append(
                    int(numstack.pop()) * int(numstack.pop())
                )
            elif t == '/':
                b = int(numstack.pop())
                a = int(numstack.pop())
                # print(a,b)
                negs = 0
                if b < 0:
                    negs += 1
                if a < 0:
                    negs += 1
                ansneg = 1
                if negs % 2 == 1:
                    ansneg = -1
                numstack.append(
                    abs(a) // abs(b) * ansneg
                )
            elif t == '-':
                b,a = numstack.pop(),numstack.pop()
                numstack.append(
                    int(a) - int(b)
                )
            print(t,numstack)
        return int(numstack[0])