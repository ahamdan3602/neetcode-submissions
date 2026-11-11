class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for token in tokens:
            if self.is_numeric(token):
                stk.append(token)
            else:
                if token == "*" and len(stk) > 1:
                    f_val = int(stk.pop())
                    s_val = int(stk.pop())
                    stk.append(f_val * s_val)
                elif token == "/" and len(stk) > 1:
                    f_val = int(stk.pop())
                    s_val = int(stk.pop())
                    stk.append(s_val / f_val)
                elif token == "+" and len(stk) > 1:
                    f_val = int(stk.pop())
                    s_val = int(stk.pop())
                    stk.append(f_val + s_val)
                elif token == "-" and len(stk) > 1:
                    f_val = int(stk.pop())
                    s_val = int(stk.pop())
                    stk.append(s_val - f_val)

        return int(stk[-1])


    def is_numeric(self, value):
        try:
            float(value)  # Converts positive/negative integers and decimals smoothly
            return True
        except (ValueError, TypeError):
            return False
