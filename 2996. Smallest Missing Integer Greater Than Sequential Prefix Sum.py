class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Set the sequence equal to the first element, because regardless of the next nums value, the prefixSum will always contain the first value
        prefixSum = nums[0]
        
        # Check the rest of the values to see if they are sequential from the starting value, excluding the first index since we already accounted for that
        for i in range(1, len(nums)):

            # If sequential, current index should equal to previous index + 1, if it does not, this nums[index] value is not sequential
            if nums[i] != nums[i - 1] + 1:
                # Therefore, break, we know the prefixSum
                break
            # else nums[i] == nums[i - 1] + 1:
            else: 
                # The number prior equals this number, so they are sequential
                # Add sequential value to prefixSum
                prefixSum += nums[i]
        
        # Return the smallest integer X missing from nums such that X is greater than or equal to the sum of the longest sequential prefix

        # While prefixSum in nums, increment by 1
        while prefixSum in nums:
            prefixSum += 1
            
        return prefixSum
