class TrieNode:
    def __init__(self):
        self.is_leaf = False
        self.chars = [None]*26

    def insert(self, word: str) -> None:
        node = self
        for c in word:
            i = ord(c) - ord('a')
            if not node.chars[i]:
                node.chars[i] = TrieNode()

            node = node.chars[i]

        node.is_leaf = True

    def search(self, word: str) -> bool:
        node = self
        for c in word:
            i = ord(c) - ord('a')
            if not node.chars[i]:
                return False

            node = node.chars[i]

        return node is not None and node.is_leaf

class Solution:
    def __init__(self):
        self.res = set()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Insert into the Trie
        root = TrieNode()
        for word in words:
            root.insert(word)
        # print(root.search("bat"))
        # print(root.search("cat"))
        # print(root.search("back"))
        # print(root.search("backend"))
        # print(root.search("stack"))
        
        # DFS Prep
        R = len(board)
        C = len(board[0])
        visited = set() # [[False]*C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                self.dfs(r,c,R,C,board,visited,root,"")

        return list(self.res)

    def dfs(self, r: int, c: int, R: int, C: int, board: List[List[str]], visited: set, node: TrieNode, word: str) -> None:
        if r < 0 or c < 0 or r >= R or c >= C or (r,c) in visited:
            return

        ch = board[r][c]
        i = ord(ch) - ord('a')
        if not node.chars[i]:
            return

        new_word = word+ch
        # print("W: ", new_word)
        if node.chars[i].is_leaf:
            self.res.add(new_word)
            # Optimization: Optional, but don't set is_leaf to False yet 
            # because it might be a prefix for a longer word

        visited.add((r, c))
        self.dfs(r+1, c, R, C, board, visited, node.chars[i], new_word)
        self.dfs(r-1, c, R, C, board, visited, node.chars[i], new_word)
        self.dfs(r, c+1, R, C, board, visited, node.chars[i], new_word)
        self.dfs(r, c-1, R, C, board, visited, node.chars[i], new_word)

        visited.remove((r,c))