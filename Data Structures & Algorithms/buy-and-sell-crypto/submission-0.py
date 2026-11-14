class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                max_p = max(prices[j] - prices[i], max_p)
        
        return max_p