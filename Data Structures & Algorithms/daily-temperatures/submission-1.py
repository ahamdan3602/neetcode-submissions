class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        return array result, where result[i] = # of days after the ith day before a warmer temperature appears on a future day
        
        
        stk = []

        '''
        res = len(temperatures) * [0]

        for i in range(len(temperatures)):
            for j in range(i, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    res[i] = j-i
                    break
        return res