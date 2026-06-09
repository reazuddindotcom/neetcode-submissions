class Solution:
    # V0: WITHOUT DP
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return False

        total = 0
        for n in nums:
            total += n

        if total % 2:
            return False

        return self.dfs(nums, 0, total/2)

        
        
    def dfs(self, nums: List[int], i: int, t: int) -> bool:
        if t == 0:
            return True

        if i >= len(nums) or t < 0:
            return False

        if self.dfs(nums, i+1, t-nums[i]):
            return True

        return self.dfs(nums, i+1, t)