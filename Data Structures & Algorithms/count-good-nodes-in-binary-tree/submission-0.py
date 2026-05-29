# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.goodCount(root, -200, 0)

    def goodCount(self, node: TreeNode, max_v: int, count: int) -> int:
        if not node:
            return count

        if node.val >= max_v:
            max_v = node.val
            count += 1
        print(node.val, max_v, count)

        l_count = self.goodCount(node.left, max_v, count)
        count = max(count, l_count)

        r_count = self.goodCount(node.right, max_v, count)
        count = max(count, r_count)

        return count

        

        
        