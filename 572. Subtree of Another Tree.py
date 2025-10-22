# Time Complexity: O(n * m)
# Space Complexity: O(n + m)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: 
            return True
        # subRoot exists, but root does not
        if not root:
            return False
        
        # Check from the root of root if subroot is a subset
        if self.sameTree(root, subRoot):
            return True
        # Check if root.left and root.right are subtrees, recursively
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))
        
    # Helper function to compare the current position in the root to the entire subRoot
    def sameTree(self, t: Optional[TreeNode], s: Optional[TreeNode]) -> bool:
        # A null subroot can be a subset
        if not t and not s:
            return True
        if t and s and t.val == s.val:
            return (self.sameTree(t.left, s.left) and
                    self.sameTree(t.right, s.right))
        return False
