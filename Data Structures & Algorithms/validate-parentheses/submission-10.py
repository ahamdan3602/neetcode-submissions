class Solution:
    def isValid(self, s: str) -> bool:
        stk = []

        if len(s) == 1:
            return False


        for c in s:
            if c in "[({":
                stk.append(c)
                print(c)
            else:
                if len(stk) == 0:
                    return False
                if c == ']' and stk[-1] == '[':
                    stk.pop()
                elif c == ')' and stk[-1] == '(':
                    stk.pop()
                elif c == '}' and stk[-1] == '{':
                    stk.pop()
                else:
                    return False

        print(stk)
        if len(stk) != 0:
            return False
        return True
        