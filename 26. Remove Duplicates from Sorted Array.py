class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        found = set()  # Set to contain all ints we have encountered
        unique = 0  # keeps count of index, and how many unique ints there are
        for n in nums:
            if n not in found:  # If n is unique compared to all prior ints
                nums[unique] = n  # Set current n to index where all previous values to index are unique
                found.add(n)  # Add n to the set so we know any more occurrences of n are not unique
                unique += 1

        return unique
