# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        balanced, _ = self.checkBalance(root)
        return balanced
        
    def checkBalance(self, root: Optional[TreeNode]) -> [bool, int]:
        if not root:
            return [True, 0]

        l_balanced, lh = self.checkBalance(root.left)
        r_balanced, rh = self.checkBalance(root.right)

        if not l_balanced or not r_balanced:
            return [False, 0]

        if abs(lh-rh) > 1:
            return [False, 0]

        return [True, max(lh, rh) + 1]
