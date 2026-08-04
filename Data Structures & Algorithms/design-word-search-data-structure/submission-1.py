class TreeNode:
    def __init__(self):
        self.is_leaf = False
        self.chars = [None]*26

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not node.chars[i]:
                node.chars[i] = TreeNode()

            node = node.chars[i]

        node.is_leaf = True
        

    def search(self, word: str) -> bool:
        return self.searchNode(word, self.root)

    def searchNode(self, word: str, node: TreeNode) -> bool:
        for i in range(len(word)):
            c = word[i]
            if c == '.':
                # recurse and return from new search
                for r in "abcdefghijklmnopqrstuvwxyz":
                    if self.searchNode(r + word[i+1:], node):
                        return True
                return False
            else:
                idx = ord(c) - ord('a')
                if not node.chars[idx]:
                    return False

            node = node.chars[idx]

        return node.is_leaf # node is not None and 
        
