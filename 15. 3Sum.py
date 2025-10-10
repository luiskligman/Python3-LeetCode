# Time Complexity O(n^2)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # For two two-pointer to work, the data must be sorted
        toRet = []  # Create an empty list that will be used to return the triplets

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue  # prev number is the same as current, prevent duplicate output

            l, r = i + 1, len(nums) -1  # Create two pointers
            while l < r:
                sum = n + nums[l] + nums[r] # Use sum to figure out which index to update
                if sum > 0: # Sum too big, decrement right index to decrease sum value
                    r -= 1
                elif sum < 0:  # Sum too small, increment left index to increase sum value
                    l += 1
                else: 
                    toRet.append([n, nums[l], nums[r]])  # Sum = 0, append triplet pair to toRet
                    l += 1  # Increment left index to start checking for more triplet pairs
                    while nums[l] == nums[l - 1] and l < r:  # If l val == prev l val, shift l forward again as long as l does not become bigger than r
                        l += 1

        return toRet
