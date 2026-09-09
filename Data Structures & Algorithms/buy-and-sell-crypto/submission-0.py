class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')

        for item in prices: 
            max_profit = max(max_profit, item - min_price)
            min_price = min(min_price, item)

        return max_profit
