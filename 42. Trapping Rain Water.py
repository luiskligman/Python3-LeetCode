# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0

        l, r = 0, len(height) - 1  # Two pointers, start and end
        # Store the max value found starting from the left side, store the max value starting from the right side
        leftMax, rightMax = height[l], height[r]  
        # This will be the value that contains how much water we can trap
        ret = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                ret += leftMax - height[l]
            else: 
                r -= 1
                rightMax = max(rightMax, height[r])
                ret += rightMax - height[r]
        return ret
