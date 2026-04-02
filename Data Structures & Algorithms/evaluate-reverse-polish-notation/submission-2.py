class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        for token in tokens:
            if token == '+':
                num1 = numStack.pop(-1)
                num2 = numStack.pop(-1)
                numStack.append(num2 + num1)
            elif token == '-':
                num1 = numStack.pop(-1)
                num2 = numStack.pop(-1)
                numStack.append(num2 - num1)
            elif token == '*':
                num1 = numStack.pop(-1)
                num2 = numStack.pop(-1)
                numStack.append(num2 * num1)
            elif token == '/':
                num1 = numStack.pop(-1)
                num2 = numStack.pop(-1)
                numStack.append(int(num2 / num1))
            else:
                numStack.append(int(token))
        return numStack[0]
        