# USE self. instead of Solution(). because Solution(). will create an entirely new object in memory
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1  # Create the left and right bound pointers
        return self.binarySearch(l, r, nums, target)

    def binarySearch(self, l: int, r: int, nums: list, target: int) -> int:
        if l > r:  # If pointers crossover, there must be an error, return not found value of -1
            return -1
        mid = (r + l) // 2  # calculate mid point, r = 10, l = 0, (10 + 0) // 2 == 5
        if nums[mid] == target:  # We found the target value, return index of occurrence
            return mid
        elif nums[mid] > target:  # Eliminate top half of nums
            return self.binarySearch(l, mid - 1, nums, target)
        else:  # Eliminate bottom half of nums
            return self.binarySearch(mid + 1, r, nums, target)
