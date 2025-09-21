class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Create a hashset called set that we will add each value into, this way we can solve the problem in one pass of the list nums
        hashset = set()

        # Iterate through nums
        for n in nums:
            #  if n is in the hashset, then our hashset set then this value n would cause a duplicate
            if n in hashset:
                return True  # If duplicate found, return true
            hashset.add(n)  # If n was not a duplicate, add it to the hashset
        
        # Return false since no duplicate was found
        return False
