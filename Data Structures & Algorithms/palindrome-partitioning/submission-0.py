class Solution:
    def __init__(self):
        self.results = []
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []

        self.results = []
        self.allPartitions(s, 0, 0, [])

        return self.results

    def allPartitions(self, s: str, i: int, j: int, parts: List[str]) -> None:
        if j == len(s):
            return

        if self.isPal(s, i, j):
            # print("append", i, j, s[i:j+1])
            parts.append(s[i:j+1])
            if j == len(s)-1:
                self.results.append(list(parts))
                parts.pop() # CORRECTED NEEDED
                return

            self.allPartitions(s, j+1, j+1, parts)
            parts.pop()

        self.allPartitions(s, i, j+1, parts)
        

    def isPal(self, s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True