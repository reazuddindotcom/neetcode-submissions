# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checkMinMax(root, float("-inf"), float("inf"))

    def checkMinMax(self, node: Optional[TreeNode], minv: int, maxv: int) -> bool:
        if not node:
            return True

        if node.val <= minv or node.val >= maxv:
            return False

        left_bst = self.checkMinMax(node.left, minv, min(maxv, node.val))
        if not left_bst:
            return False

        right_bst = self.checkMinMax(node.right, max(minv, node.val), maxv)

        return right_bst

        
        