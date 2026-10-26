class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0 
        max_profit = 0
        for end in range(len(prices)):
            max_profit = max(max_profit, prices[end] - prices[start])
            while prices[start] > prices[end] and start < end:
                start+=1
        return max_profit