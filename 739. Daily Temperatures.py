# Monotonic Decreasing Stack
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t, in enumerate(temperatures):
            # If the stack is not empty, and is this temperature greater than the temperature on the top of our stack
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()  
                res[stackInd] = (i - stackInd)  # i = current index, stackInd = index of temperature in temperatures list

            # Push today's temperature and index onto the stack
            stack.append([t, i])

        return res
