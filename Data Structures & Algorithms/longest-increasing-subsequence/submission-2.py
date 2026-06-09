class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        max_len = [1] * n
        max_res = 1
        for i in range(1, n, 1):
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i]:
                    max_len[i] = max(max_len[i], max_len[j]+1)

            max_res = max(max_res, max_len[i])
            print(i, nums[i], max_len[i], max_res)

        return max_res