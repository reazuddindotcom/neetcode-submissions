# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    def __init__(self):
        self.delim = '|'
        self.null = '#'
        self.strs = []
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.strs = []
        self.dfs(root)

        serialized = self.delim.join(self.strs)
        # print("serialize", serialized)
        return serialized
    def dfs(self, root: Optional[TreeNode]) -> None:
        if not root:
            self.strs.append("#")
            return
        
        self.strs.append(str(root.val))
        self.dfs(root.left)
        self.dfs(root.right)



        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        # print("deserialize: ", data)
        strs = data.split(self.delim)
        node, _ = self.construct(strs, 0)

        return node

    def construct(self, parts: List[str], idx: int) -> [Optional[TreeNode], int]:
        if idx >= len(parts):
            return None, idx
        if parts[idx] == '#':
            return None, idx

        # print("Create", int(parts[idx]))
        node = TreeNode(int(parts[idx]))
        left, next_idx = self.construct(parts, idx+1)
        node.left = left

        right, next_idx = self.construct(parts, next_idx+1)
        node.right = right

        # print("Return", node.val, next_idx)

        return node, next_idx

