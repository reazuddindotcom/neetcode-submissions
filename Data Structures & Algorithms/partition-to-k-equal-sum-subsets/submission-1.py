class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        l = len(nums)
        if k > l:
            return False

        s = sum(nums)
        if s % k != 0:
            return False

        nums.sort(reverse=True)

        sums = [0]*k
        return self.dfs(nums, 0, k, sums, s//k)

    def dfs(self, nums, s, k, sums, target):
        if s == len(nums):
            return True

        for i in range(k):
            if i > 0 and sums[i] == sums[i-1]:
                continue
            if sums[i]+nums[s] <= target:
                sums[i] = sums[i] + nums[s]
                if self.dfs(nums, s+1, k, sums, target):
                    return True
                sums[i] = sums[i] - nums[s]
            
            if sums[i] == 0:
                break

        return False

    # [10,1,10,9,6,1,9,5,9,10,7,8,5,2,10,8]
    # 11