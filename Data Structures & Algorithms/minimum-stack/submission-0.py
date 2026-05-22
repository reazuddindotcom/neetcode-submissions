class MinStack:
    # self.min_val = float('inf')
    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            if val <= self.min_stack[-1]:
                self.min_stack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return
        # min_stack cannot be empty before stack
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()


    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]
        

    def getMin(self) -> int:
        if not self.min_stack:
            return None
        return self.min_stack[-1]
        

# while popping scan the entire stack O(n) 
# top = val - min
# val = top + min
# 3, 2, 2, 4, 1
# S:
# mS: