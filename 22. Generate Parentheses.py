# Solution involves using a stack combined with recursive calls
# Time Complexity:  # More complex than what I currently know about solving for big O notation
# Space Complexity: O(n)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open parenthesis if open < n
        # only add a closing parenthesis if close < open
        # valid if open == close == n

        stack = []  # holds parenthesis
        res = []  # holds list of valid parenthesis combinations

        def backtrack(openN, closedN):
            if openN == closedN == n:  # we must be finished
                res.append("".join(stack))  # append entire string 'stack' to res 
                return

            if openN < n:
                stack.append('(')  # add open parenthesis
                backtrack(openN + 1, closedN)  # Recursive call, adding an open parenthesis
                stack.pop()  # pop open parenthesis off of stack because backtrack() will handle this path

            if closedN < openN:
                stack.append(')')  # add close parenthesis
                backtrack(openN, closedN + 1)  # Recursive call, adding a close parenthesis
                stack.pop()  # pop closed parenthesis off of stack because backtrack() will handle this path

        backtrack(0, 0)  # initial call to start backtrack, will initially default to starting with an open parenthesis
        return res
