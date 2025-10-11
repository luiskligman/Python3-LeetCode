# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time Complexity: O(n + m)
# Space Complexity: O(1)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode()

        while list1 and list2:  # While both lists exist
            if list1.val < list2.val:  
                tail.next = list1  # Make the pointer point to smallest value
                tail = tail.next  # Update the new linked list
                list1 = list1.next  # Iterate list1
            else:  # Else, list2 had the smaller value
                tail.next = list2  # Make the pointer point to the next smallest value, list2 in this case
                tail = tail.next  # Iterate the new linked list
                list2 = list2.next  # Iterate list2
        tail.next = list1 or list2  # Append whichever list still has elements to the new linked list, able to do since we know both given lists are already sorted

        return dummy.next  # Return the next node from dummy, dummy.val = 0
        
        
