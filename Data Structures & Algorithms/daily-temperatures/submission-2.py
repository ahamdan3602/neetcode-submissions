class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # Initialize result array with 0s. 
        # If a day never finds a warmer temp, it correctly stays 0.
        res = [0] * len(temperatures)
        
        # Stack will store indices of temperatures, not the temperatures themselves.
        stk = [] 
        
        for i, temp in enumerate(temperatures):
            # While stack is not empty AND current temp is warmer than 
            # the temperature at the index stored at the top of the stack
            while stk and temp > temperatures[stk[-1]]:
                # We found a warmer day for a previous day!
                prev_idx = stk.pop()
                
                # Calculate the difference in days and store it in the result array
                res[prev_idx] = i - prev_idx
            
            # Add the current day's index to the stack to wait for a warmer day
            stk.append(i)
            
        return res