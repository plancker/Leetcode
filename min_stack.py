class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.mstack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.mstack) > 0:
            if x < self.mstack[0]:
                n = [x]
                n.extend(self.mstack)
                self.mstack = n
            else:
                self.mstack.append(x)
        else:
            self.mstack.append(x)

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.mstack[-1]:
            self.mstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mstack[-1]
