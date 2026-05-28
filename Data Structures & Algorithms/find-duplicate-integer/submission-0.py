class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        prev = nums[i]
        while i < len(nums):
            idx = abs(nums[i]) # idx-1 is not necessary, since 
            if nums[idx] < 0:
                return idx

            nums[idx] = -nums[idx]
            i += 1

        