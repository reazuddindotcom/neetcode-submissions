class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in "+-*/":
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(self.operate(op2, op1, t))
            else:
                stack.append(t)
        return int(stack[-1])

    def operate(self, op1: str, op2: str, op: str) -> int:
        if op == '+':
            return int(op1) + int(op2)
        if op == '-':
            return int(op1) - int(op2)
        if op == '*':
            return int(op1) * int(op2)
        if op == '/':
            return int(int(op1)/int(op2))

# Edge1: ["10","6","9","3","+","-11","*","/","*","17","+","5","+"] ## (10*(6/((9+3)*(-11))))+17+5: “//” and “/” not the same.
# Edge2: ["18"]