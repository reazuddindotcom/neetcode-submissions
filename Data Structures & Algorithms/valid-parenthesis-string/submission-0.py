class Solution:
    def checkValidString(self, s: str) -> bool:
        left_p = []
        stars = []

        for i in range(len(s)):
            c = s[i]
            if c == '(':
                left_p.append(i)
            if c == ')':
                if left_p:
                    left_p.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
            if c == '*':
                stars.append(i)

        while left_p and stars:
            if left_p[-1] < stars[-1]:
                left_p.pop()
            stars.pop()

        return not left_p