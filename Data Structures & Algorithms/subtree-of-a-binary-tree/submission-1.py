# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return subRoot is None
        if not subRoot:
            return True
        
        if self.isSameTree(root, subRoot):
            return True

        if self.isSubtree(root.left, subRoot):
            return True

        return self.isSubtree(root.right, subRoot)
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        if p.val != q.val:
            return False

        if not self.isSameTree(p.left, q.left):
            return False

        return self.isSameTree(p.right, q.right)