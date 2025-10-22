# Time Complexity: O(n)
# Space Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If p and q both don't exist, return true, they are equal
        if not p and not q:
            return True
        # If p and q exist and p.val == q.val, then check if the left and right parts are equal
        # Only return true if both sides are equal
        elif p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # If p exists and q does not, return false, vice versa
        else: 
            return False


                
