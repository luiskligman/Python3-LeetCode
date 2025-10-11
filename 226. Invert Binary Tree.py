# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:  # If root does not exist, base case
            return None

        # Swap right and left roots
        temp = root.left 
        root.left = root.right
        root.right = temp

        # Recursive call to invert the children
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
