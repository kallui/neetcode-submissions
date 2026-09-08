class MinStack:
    def __init__(self):
        self.stack = [] # TUPLE (VALUE, MINIMUM AT THAT POINT AND BELOW)

    def push(self, val: int) -> None:
        minimum = 0
        if len(self.stack) == 0:
            minimum = val
        else:
            minimum = min(val, self.stack[-1][1])
        self.stack.append((val, minimum))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
