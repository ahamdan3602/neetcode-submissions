class MinStack:

    def __init__(self):
        self.stk = []
        self.min_elem = float('inf')
        self.min_elems = []

    def push(self, val: int) -> None:
        if val <= self.min_elem:
            self.min_elem = val
            self.min_elems.append(val)

        self.stk.append(val)

    def pop(self) -> None:
        if not self.stk:
            return
        if self.top() == self.min_elem:
            self.min_elems.pop()
            if self.min_elems:
                self.min_elem = self.min_elems[-1]
            else:
                self.min_elem = float('inf')
        self.stk.pop()
        

    def top(self) -> int:
        if not self.stk:
            return -1
        return self.stk[-1]

    def getMin(self) -> int:
        return int(self.min_elem)
