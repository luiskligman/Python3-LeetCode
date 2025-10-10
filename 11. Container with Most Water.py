class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) -1
        maxWater = 0
        while l < r:  # While pointers are not equal and have not crossed over
            # Determine the maxWater that can be held, by finding the max. value of either maxWater or by calculating the volume of the current container depending on the lesser height value and the containers width
            maxWater = max(maxWater, (min(height[l], height[r]) * (r - l)))
            if height[l] <= height[r]:  # Increment the index pointing to the lesser height; if heights are equal, increment the left index
                l += 1
            else: 
                # Right index points to a lesser height
                r -= 1
        return maxWater

