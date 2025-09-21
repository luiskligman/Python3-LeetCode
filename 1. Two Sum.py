class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create an empty map, keys will be the number, values will be the index that the number occurs at
        map = {}

        for i, n in enumerate(nums):
            # Figure out what other number we would need to have an answer that equals the target
            # Target = diff + n --> diff = target - n
            diff = target - n
            # Since we need a number diff to add up to equal the target, check if we have that number by checking the map
            if diff in map:
                # If we have it, return the value for that number first, since it will be a smaller index, then return the current index i
                return [map[diff], i]
            # Since we didn't have what we needed to sum to the target, add the current number to the map as key, and add the index of occurrence as value
            map[n] = i
        return  # Return empty list
