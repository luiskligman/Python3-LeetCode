# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            start = i  # we state that this height is guaranteed to have a width of 1 starting at this index, we will later find out if this height is applicable for new or 
                       # previous elements, hence we might update the start index 
            # While the stack is not empty and the height of the previous stack's element is greater than the current height
            while stack and stack[-1][1] > h:
                index, height = stack.pop()  # Pop that element because it can no longer be extended forward with that height, because the new element has a lesser height
                maxArea = max(maxArea, height * (i - index))  # Compute the max area of the element we just popped, considering how far back/forward it could have extended
                start = index  # Pushing back the starting index of the current element we are trying to add, since that height would fit in previous entries, we want to figure out how many previous entries it was able to fit into
            stack.append((start, h))  # Append the new element with the start being however many entries previous this element's height is within, 

        # Elements in the stack when we reach the end of heights
        for i, h in stack:
            # Compute max area using the elements' height and their width. Since we are at the end, we just need to minus the start index from the total length of the given list heights
            maxArea = max(maxArea, h * (len(heights) - i))
    
        # Return the maxArea we found from the operation
        return maxArea
        
