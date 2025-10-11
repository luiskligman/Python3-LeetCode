# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:  # While curr != None
            temp = curr.next  # Store the link to next
            curr.next = prev  # Make curr.next point backwards
            prev = curr  # Shift forward
            curr = temp  # Shift forward using stored link
        return prev  # Once curr == None prev must be the head
