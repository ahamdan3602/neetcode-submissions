import sys
class MinStack:

    def __init__(self):
        self.stk = []
        self.minVal = sys.maxsize
        self.minVals = []
        self.minIdx = -1

    def push(self, val: int) -> None:
        # self.minVal = min(self.minVal, val)
        print(val)
        if self.minVal >= val:
            self.minVal = val
            self.minVals.append(self.minVal)
            self.minIdx = len(self.stk)
        print(self.minVals)
        self.stk.append(val)

    def pop(self) -> None:
        # If the value leaving the stack is the current minimum
        if self.stk[-1] == self.minVal:
            self.minVals.pop()
            # Correctly update self.minVal to the previous minimum
            if self.minVals:
                self.minVal = self.minVals[-1]
            else:
                self.minVal = sys.maxsize # Or sys.maxsize
        self.stk.pop()
            

    def top(self) -> int:
        return self.stk[-1]
        
    def getMin(self) -> int:
        return self.minVal
        
