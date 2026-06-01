# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.in_ord_map = {}
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        for i in range(len(inorder)):
            self.in_ord_map[inorder[i]] = i

        return self.buildTreeDfs(preorder, inorder, 0, len(inorder)-1, 0)
        #TEST Video Code TEST
        # if not preorder or not inorder:
        #     # print("None")
        #     return None

        # root = TreeNode(preorder[0])
        # # print("Create ", preorder[0])
        # mid = inorder.index(preorder[0])
        # # print("Mid ", mid)
        # # print("Go left")
        # root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        # # print("Go right")
        # root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        # return root

    def buildTreeDfs(self, preorder: List[int], inorder: List[int], in_s: int, in_e: int, pre_s: int) -> Optional[TreeNode]:
        if in_s > in_e:
            print("None")
            return None

        if in_s == in_e:
            print("Create ", inorder[in_s])
            return TreeNode(inorder[in_s])

        in_ord_idx = self.in_ord_map[preorder[pre_s]]
        print(in_s, in_e, pre_s, preorder[pre_s], in_ord_idx)
        node = TreeNode(preorder[pre_s])
        print("go left")
        left_node = self.buildTreeDfs(preorder, inorder, in_s, in_ord_idx -  1, pre_s+1)

        print("go right")
        # pre_s + (in_ord_idx-in_s+1) fixed the Infinite Recursion #1 issue
        # One sided tree is not in the test cases
        right_node = self.buildTreeDfs(preorder, inorder, in_ord_idx+1, in_e, pre_s + (in_ord_idx-in_s+1))

        node.left = left_node
        node.right = right_node

        return node

# Infinite Recursion #1
# preorder=[8,4,2,1,3,6,5,7,12,10,9,11,14,13,15]
# inorder= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# print(in_s, in_e, pre_s, preorder[pre_s], in_ord_idx)

# Wrong Answer (one sided tree)
# [1,1,1,1,1,1,2]
# [1,1,1,1,1,2,1]