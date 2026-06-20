class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l = len(nums)
        for i in range(l):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(l):
            idx = abs(nums[i])-1
            if idx >=0 and idx < l:
                if nums[idx] > 0:
                    nums[idx] = -nums[idx]
                elif nums[idx] == 0:
                    nums[idx] = -(l+1)

        for i in range(l):
            if nums[i] >= 0:
                return i+1

        return l+1