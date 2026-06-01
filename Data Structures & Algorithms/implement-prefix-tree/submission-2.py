
class TreeNode:
    def __init__(self):
        self.is_leaf = False
        self.chars = [None]*26

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()
        

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not node.chars[i]:
                node.chars[i] = TreeNode()

            node = node.chars[i]

        node.is_leaf = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not node.chars[i]:
                return False

            node = node.chars[i]

        return node is not None and node.is_leaf
        
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            i = ord(c) - ord('a')
            if not node.chars[i]:
                return False

            node = node.chars[i]

        return node is not None
        
        