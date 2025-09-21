# Time Complexity: O(nlogn); iterating through each car + inital sort on position
# Space Complexity: O(n)
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # The built-in Python function zip() takes two (or more) iterables and combines them element-by-element into tuples
        # Using list comprehension, we take the tuple (p, s), unpack it to p and s, then build [p, s]
        pair = [[p, s] for p, s in zip(position, speed)]

        stack = []
        # sorted() will sort a list or lists (or tuples) by the first element, and if those are equal, it uses the second element
        # Using [::-1] reverses the entire list, [start:stop:step], leaving start and stop empty. It means to use the entire list, step = -1 means move backwards by 1 each step
        for p, s in sorted(pair)[::-1]:  # Reverse Sorted Order
            stack.append((target - p) / s)  # figure out time of arrival in decimal form, (target - currentPosition) / travelingSpeed. ex (10 - 3) / 3 = 2.33
            # If the stack has at least two arrival times
            # If the newly added arrival time is less (meaning it will approach the end faster) than the car in front of it (since we are working in reverse order), then it will become a fleet,   
            # hence the front car will limit the second car, therefore, we can pop the car (arrival time) we just added to the stack because they become one, arriving at the same time
            if len(stack) >= 2 and stack[-1] <= stack[-2]:  
                stack.pop()
        return len(stack)
