class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            # nums[l] < nums[r] would mean subset between l and r is sorted
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
        
            m = (l + r) // 2
            res = min(res, nums[m])
            # if nums[m] greater than nums[l], then we know this subset is sorted with no pivot, therefore, pivot value must be on the right side, update pointers
            if nums[m] >= nums[l]:
                l = m + 1
            # else nums[m] < nums[l], the pivot must be between these two indexes, adjust pointers
            else:
                r = m - 1
            
        return res
