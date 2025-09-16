class MinStack:

    def __init__(self):
        self.stack = []
        # Use this stack to keep track of what the minimum value in the stack is for all values
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Taking the minimum value of either value or the last element in minStack if minStack is not empty else if minStack is empty, make the min compare val to val to prevent index errors
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]      


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
