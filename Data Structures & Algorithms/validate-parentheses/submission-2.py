class Solution:
    def isValid(self, s: str) -> bool:
        paren_map = {')':'(', ']':'[', '}':'{'}
        stack = []
        for i in s:
            if i == ')' or i == ']' or i == '}':
                if stack and stack[-1] == paren_map[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        print(len(stack))
        return len(stack) == 0