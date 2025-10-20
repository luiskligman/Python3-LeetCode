# IF YOU SEE THIS MESSAGE, REVIEW THIS PROBLEM & 153

# Time Complexity: O(logn)
# Space Complexity: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1
        res = nums[l]

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            # left of mid is sorted, right contains pivot
            elif nums[l] <= nums[m]:   
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1

            # left of mid is not sorted, contains pivot
            else: 
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        return -1
