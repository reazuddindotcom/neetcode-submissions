class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_sum = float("-inf")
        cur_sum = 0
        j = 0
        while j < len(nums):
            cur_sum += nums[j]
            max_sum = max(max_sum, cur_sum)
            # print(j, cur_sum, max_sum)
            j += 1
            if cur_sum < 0:
                cur_sum = 0
            
        return max_sum