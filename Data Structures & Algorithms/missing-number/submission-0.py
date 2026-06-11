class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = 0
        for i in range(len(nums)+1):
            missing ^= i

        for n in nums:
            missing ^= n

        return missing