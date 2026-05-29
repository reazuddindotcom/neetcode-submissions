# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_d = 0
        
        def getDiameter(root):
            nonlocal max_d
            
            if not root:
                return 0

            lh = getDiameter(root.left)
            rh = getDiameter(root.right)

            max_d = max(max_d, (lh+rh))

            return max(lh, rh) + 1

        getDiameter(root)
        return max_d