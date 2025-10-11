# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        if len(prices) < 2:  # If the length is less than 2, we can't buy and sell
            return 0
        
        l, r = 0, 1  # Two pointers, l starts at first index, r starts at next index
        while r in range(len(prices)):  
            # Calculate the maxProf of the current window, then see if l needs to be updated or only r, r will get updated on every iteration
            maxProf = max(maxProf, prices[r] - prices[l])  # Determine the current maxProf based on the window
            if prices[r] < prices[l]:  # If r points to a lesser price than l, update window 
                l = r
            r += 1  # Iterate r to the next index

        return maxProf
