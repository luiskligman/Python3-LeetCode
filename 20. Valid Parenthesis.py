# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')':'(', '}':'{', ']':'['}

        for c in s:
            if c in closeToOpen:
                # We cannot add a closing parenthesis to an empty stack

                # stack checks if the stack is empty
                # stack[-1] is the last item that was added to the stack
                # We compare the last item added with the complement of the closing brace we currently have
                # if the last element of the stack is the opening bracket to this closing bracket, we can pop that off the stack
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else: 
                    return False
            else: 
                # if the character is not a closing bracket, append it to the stack
                stack.append(c)

        # use not stack because stack returns false when empty, we want the stack to be empty
        return True if not stack else False
