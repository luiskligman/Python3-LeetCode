class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        l = r = 0
        output = []

        while r < len(nums):
            # While q is not empty and the lowest value in the queue is less than nums at index r
            while q and nums[q[-1]] < nums[r]:
                q.pop()  # pop the lowest values from the queue
            q.append(r)  # append the new r value to the queue
                         # will be in position q[0] if it is the greatest value

            # l index value falling exiting window
            if l > q[0]:    
                q.popleft()

            # if length of the window is k, append the largest value from the monotonic stack
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output
            
        
