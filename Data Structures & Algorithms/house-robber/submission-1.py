class Solution:
    def rob(self, nums: List[int]) -> int:
        # Q: Is skipping multiple an option?? Yes.
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        max_rob = [0]*n
        max_rob[0] = nums[0]
        max_rob[1] = max(nums[0],nums[1])

        for i in range(2, n, 1):
            max_rob[i] = max(max_rob[i-2]+nums[i], max_rob[i-1])

        return max_rob[n-1]
        