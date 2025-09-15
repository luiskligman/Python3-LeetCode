# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # IDEA FOR SOLUTION:
        # Pass through the array and populate the res array first with all of the products of numbers before the specific index
        # Then pass through the array again, get the product of all the numbers after index
        # Finally, multiply pre and post to get the product of all numbers that are not at specific index
        # Update the pre or post as you are moving


        # Populate an array with initial values of 1, size must be the length of nums
        res = [1] * (len(nums))

        # Use the prefix to say that the product of all numbers before the first number in nums is 1
        prefix = 1

        # Iterate through nums start to end
        for i in range(len(nums)):
            # Set res at specific index to prefix
            res[i] = prefix  
            # Update prefix
            prefix *= nums[i]
        
        # Postfix should also be 1, working end to start, there are no elements after the end of nums, therefore, postfix = 1
        postfix = 1

        # Iterate through nums end to start
        for i in range(len(nums) - 1, -1, -1):
            # Multiply current res value from previous for loop by postfix
            res[i] *= postfix
            # Update postfix
            postfix *= nums[i]

        # Simply return filled in array
        return res
        
