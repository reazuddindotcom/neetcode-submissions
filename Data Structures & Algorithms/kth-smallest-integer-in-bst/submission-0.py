# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        kth, _, _ = self.kthSmallestDfs(root, k, 0)

        # always available
        return kth
        
    def kthSmallestDfs(self, node: Optional[TreeNode], k: int, count: int) -> [int, int, bool]: # kth num, count, found
        if not node:
            return [0, count, False]

        kth, l_count, found = self.kthSmallestDfs(node.left, k, count)
        if found:
            return [kth, l_count, found]
        # visit this node
        count = l_count + 1
        if count == k:
            return [node.val, count, True]

        return self.kthSmallestDfs(node.right, k, count)
