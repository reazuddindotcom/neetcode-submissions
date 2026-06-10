class Solution:
    # V0: Without DP --> Got TLE as expected.
    # V1: With DP
    def __init__(self):
        self.max_c = {}
    def maxCoins(self, nums: List[int]) -> int:
        # Q What happens to the adjacent ballons if we burst a balloon?
        # They come together and become neighbors?
        x_nums = [1, *nums, 1]
        return self.dfs(x_nums, 1, len(nums))

    def dfs(self, nums: List[int], l: int, r: int) -> int:
        if l > r:
            return 0
        # if l == r: # Not needed. Handled by the cases below
        #     return nums[l] * nums[l - 1] * nums[l + 1]

        if (l,r) in self.max_c:
            return self.max_c[(l,r)]

        max_v = 0
        for i in range(l, r + 1, 1):
            left = self.dfs(nums, l, i - 1)
            right = self.dfs(nums, i + 1, r)
            cur = nums[i] * nums[l - 1] * nums[r + 1]

            max_v = max(max_v, (left + right + cur))

        self.max_c[(l,r)] = max_v

        return self.max_c[(l,r)]

# TLE Input
# [50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50]