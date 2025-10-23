class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            # first = -8, second = -7
            if second > first:
                # first - second = -8 + 7 = - 1, preserves negative order
                heapq.heappush(stones, first - second)
            # If second == first, only pop from heap
        # Push 0 so that if the heap is empty, we will just return 0
        heapq.heappush(stones, 0)
        # Convert back to positive
        return abs(stones[0])
