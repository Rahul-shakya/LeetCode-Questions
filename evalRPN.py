class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {'+', '-', '*', '/'}
        for currVal in tokens:
            if currVal not in operands:
                stack.append(currVal)
            else:
                x = int(stack.pop())
                y = int(stack.pop())
                res = x + y if currVal == '+' else y - x if currVal == '-' else x * y if currVal == '*' else int(y / x)
                stack.append(res)
        return int(stack[-1])
