class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # array is non-empty
        result = 0
        for n in nums:
            result = result ^ n

        return result