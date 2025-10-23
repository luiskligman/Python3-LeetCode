class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Store distance, and coordinates in a tuple (distance, [x, y])
        # Heap will sort based on distance, closest will be popped first
        # Append coordinates to a result list
        # Then pop this point from the heap
        res = []
        heap = []
        for p in points:
            distance = sqrt(p[0] ** 2 + p[1] ** 2)
            pair = (distance, [p[0], p[1]])
            heapq.heappush(heap, pair)

        while len(res) < k:
            res.append(heap[0][1])
            heapq.heappop(heap)

        return res
