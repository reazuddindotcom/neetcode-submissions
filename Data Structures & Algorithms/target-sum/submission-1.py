class Solution:
    # V0 Without DP --> Got accepted without DP. Lets add DP anyway.
    def __init__(self):
        self.ways = {}
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Q Confirm: using all the numbers in the array but we can only add or subtract
        # Q Each element only once?

        return self.dfs(nums, target, 0)
        

    def dfs(self, nums: List[int], target: int, i: int) -> int:
        if target == 0 and i == len(nums):
            return 1

        if i == len(nums):
            return 0

        if (target, i) in self.ways:
            return self.ways[(target, i)]

        add = self.dfs(nums, target+nums[i], i+1)
        sub = self.dfs(nums, target-nums[i], i+1)

        self.ways[(target, i)] = add+sub

        return self.ways[(target, i)]