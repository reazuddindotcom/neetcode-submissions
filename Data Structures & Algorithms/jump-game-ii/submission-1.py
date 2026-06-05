class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        min_step = [l+1]*l
        min_step[l-1] = 0

        for i in range(l-2, -1, -1):
            for j in range(i+1, i+nums[i]+1, 1):
                if j == l:
                    break
                min_step[i] = min(min_step[i], min_step[j]+1)

        return min_step[0]

