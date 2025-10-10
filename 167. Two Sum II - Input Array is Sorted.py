# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        while end > start:
            res = numbers[start] + numbers[end]
            if res > target:
                end -= 1
            elif res < target:
                start += 1
            else: 
                return [start + 1, end + 1]
        return [] 
