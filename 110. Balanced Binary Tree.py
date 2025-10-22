# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(curr):
            if not curr:
                # An empty node would be considered balanced; base case
                return [True, 0]

            # Get values for left and right sub trees, [balanced, height]
            left, right = dfs(curr.left), dfs(curr.right)
            # Check if left is balanced, right is balanced, and if the heights differ by more than 1
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            # Return balanced, and 1 + the max height, add one to account for the current node
            return [balanced, 1 + max(right[1], left[1])]
        # Return if the root is balanced
        return dfs(root)[0]
