class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        occurrences = 0  # Occurrences of val in nums
        l = len(nums)

        for n in nums:
            if n == val:
                occurrences += 1

            if n != val:
                nums[i] = n
                i += 1
        

        return l - occurrences
