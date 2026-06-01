# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max_path = float("-inf")
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.getMax(root)

        return self.max_path

    def getMax(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_max = max(self.getMax(root.left), 0)
        right_max = max(self.getMax(root.right), 0)

        self.max_path = max(self.max_path, (left_max + root.val + right_max))

        return max(root.val + left_max, root.val + right_max)

