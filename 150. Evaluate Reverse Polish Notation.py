# Time Complexity: O(2n)
# Memory Complexity: O(n)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                # (b / a ) would be decimal division, use int() to convert it to an integer, and also round it to zero
                stack.append(int(b / a))
            else:
                stack.append(int(c))

        return stack[0]
