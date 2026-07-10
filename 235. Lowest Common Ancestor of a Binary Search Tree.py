# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root  # start cur tree pointer to root

        while cur:
            # if p and q are greater than cur.val, must be in right sub tree
            if p.val > cur.val and q.val > cur.val:  
                cur = cur.right

            # if p and q are less than cur.val, must bei n the left sub tree
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left

            # either p or q == cur.val  or  p and q are on different sides from cur node
            else: 
                return cur
