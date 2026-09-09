class MinStack:

    def __init__(self):
        self.stack = []
        self.m = 100000000000000

    def push(self, val: int) -> None:
        self.m = min(self.m,val)
        print(self.m)
        self.stack.append((val,self.m))
        

    def pop(self) -> None:
        self.stack.pop()
        if self.stack: self.m = self.stack[-1][1]
        else: self.m = 100000000000000

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]