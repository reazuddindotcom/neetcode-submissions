# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max_d = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.getDiameter(root)
        return self.max_d

    def getDiameter(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        lh = self.getDiameter(root.left)
        rh = self.getDiameter(root.right)

        self.max_d = max(self.max_d, (lh+rh))

        return max(lh, rh) + 1