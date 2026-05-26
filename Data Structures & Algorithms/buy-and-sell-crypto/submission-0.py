class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        max_profit = 0
        min_val = prices[0]

        for i in range(1, len(prices), 1):
            max_profit = max(max_profit, prices[i] - min_val)
            min_val = min(min_val, prices[i])

        return max_profit

        