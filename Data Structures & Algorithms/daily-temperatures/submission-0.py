class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stk = []
        
        for i in range(n):
            while stk and temperatures[i] > temperatures[stk[-1]]:
                prev_index = stk.pop()
                res[prev_index] = i - prev_index
            stk.append(i)
        
        return res
        

    
        