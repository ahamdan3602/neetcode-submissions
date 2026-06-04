class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stk = []
        res = 0

        for token in tokens:
            if self.is_valid_int(token):
                stk.append(token)
            else:
                if token == "+":
                    val_one = stk.pop()
                    val_two = stk.pop()
                    stk.append(int(val_one) + int(val_two))
                elif token == "*":
                    val_one = stk.pop()
                    val_two = stk.pop()
                    stk.append(int(val_one)*int(val_two))
                elif token == "-":
                    val_one = stk.pop()
                    val_two = stk.pop()
                    stk.append(int(val_two)-int(val_one))
                elif token == "/":
                    val_one = stk.pop()
                    val_two = stk.pop()
                    stk.append(int(val_two)/int(val_one))
        return int(stk[-1])
    

    def is_valid_int(self, val: int) -> bool:
        try:
            int(val)
            return True
        except ValueError:
            return False

                    
                
        