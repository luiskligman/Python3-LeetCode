# Time Complexity: O(n)
# Space Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(curr) -> int:
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)

            # Add the heights from both sides
            self.res = max(self.res, left + right)
            # Add one to account for curr node
            return 1 + max(left, right)

        dfs(root)
        return self.res

        
        
