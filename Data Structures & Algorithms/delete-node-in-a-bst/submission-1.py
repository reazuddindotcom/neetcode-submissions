# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Edge: delete leaf node
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Q1 Is the node supposed to be uniqueue?
        # Q2 What if we don't find the node? Just return the tree or send another signal?

        return self.deleteNodeKey(root, key)

    def deleteNodeKey(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if root.val == key:
            print("Deleting node")
            return self.deleteThisNode(root)
        elif key < root.val:
            node = self.deleteNodeKey(root.left, key)
            root.left = node
        elif key > root.val:
            node = self.deleteNodeKey(root.right, key)
            root.right = node

        return root

    def deleteThisNode(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        lm_right = root.right
        while lm_right.left:
            lm_right = lm_right.left

        lm_right.left = root.left
        print("New root: ", root.right.val)
        return root.right

# WA   
# root=[1,null,2]
# key=2

        