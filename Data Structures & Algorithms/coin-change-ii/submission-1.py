class Solution:
    # V0 Without DP.
    # V1 Added DP. Used lessons learned. Cache result from remaining
    # part, not the cumulative values
    def __init__(self):
        self.count_map = {}
    def change(self, amount: int, coins: List[int]) -> int:
        return self.dfs(amount, coins, 0)
        
    def dfs(self, amount: int, coins: List[int], i: int) -> int:
        if amount == 0:
            return 1
        if i >= len(coins) or amount < 0:
            return -1

        if (amount, i) in self.count_map:
            return self.count_map[(amount, i)]

        total = 0
        with_c = self.dfs(amount-coins[i], coins, i)
        if with_c != -1:
            total += with_c
        without_c = self.dfs(amount, coins, i+1)
        if without_c != -1:
            total += without_c

        self.count_map[(amount, i)] = total
        return self.count_map[(amount, i)]

# TLE EXAMPLE
# amount=500
# coins=[3,5,7,8,9,10,11]