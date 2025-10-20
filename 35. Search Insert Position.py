# Time Complexity: O(log n)
# Space Complexity: O(1)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Binary search, since O(log n)
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            print(f"{l},{r},{m}")
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        # In binary search l always points to the index that could contain the target or a larger value
        return l
