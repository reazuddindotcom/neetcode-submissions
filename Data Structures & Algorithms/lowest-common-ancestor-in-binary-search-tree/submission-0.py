# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root and not p and not q:
            return None

        cur = root
        while cur:
            if p.val == cur.val or q.val == cur.val:
                return cur
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
                continue
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
                continue
            
            return cur
