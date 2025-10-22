# Time Complexity: O(n)
# Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Use Floyd's Tortoise and Hare algorithm (two-pointer technique)

# Maintain two pointers: "slow" moves one step at a time, "fast" moves two steps.

# If the list has a cycle, these pointers will eventually meet inside the loop

# If the list has no cycle, the "fast" pointer will reach the end (None) first
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
                    
        return False
            
