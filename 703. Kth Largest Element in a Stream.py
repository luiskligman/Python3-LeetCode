# Time Complexity: O(m * log k)
# Space Complexity: O(k)
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # minHeap with K largest integers
        self.minHeap, self.k = nums, k
        # Change the list 'self.minHeap' which = nums, into a heap object 
        heapq.heapify(self.minHeap)
        # Trim the heap down to only have a length of K
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        # If adding another value put us over the K limit, pop the smallest value
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        # Returns the smallest value currently stored in the heap
        return self.minHeap[0]
        
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
