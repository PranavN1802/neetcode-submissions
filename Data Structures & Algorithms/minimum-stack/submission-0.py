class MinStack:

    def __init__(self):
        self.stack = []
        self.topstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.topstack:
            min_val = self.getMin()
            if min_val < val:
                self.topstack.append(min_val)
            else:
                self.topstack.append(val)
        else: 
            self.topstack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.topstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.topstack[-1]
        
