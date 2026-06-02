class Solution:
    def __init__(self):
        self.results = []
    def generateParenthesis(self, n: int) -> List[str]:
        if not n:
            return self.results

        self.nextParen(n, n, "")

        return self.results

    def nextParen(self, left: int, right: int, parens: str) -> None:
        if not left and not right:
            self.results.append(parens)
            return

        if left:
            next_str = parens + "("
            self.nextParen(left-1, right, next_str)

        if right > left:
            next_str = parens + ")"
            self.nextParen(left, right-1, next_str)