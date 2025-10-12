# Time Complexity: O(nlog(m))
# Space Complexity: O(1)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)  # l and r are the endpoints for potential k values
        res = r  # Default return will just be the max bananas eaten per hour

        while l <= r:  # While pointers do not cross over
            k = (l + r) // 2  # Find mid point
            totalTime = 0  
            # See how much time it took to eat all the bananas given, k banana eating speed
            for p in piles:
                totalTime += math.ceil(float(p) / k)  
            # If bananas were eaten too slowly, use binary search to try the upper half
            if totalTime > h:
                l = k + 1
            # If bananas were eaten too fast, use binary search to try and find a lesser k value that still satisfies the condition
            else:
                r = k - 1
                res = k
        return res

