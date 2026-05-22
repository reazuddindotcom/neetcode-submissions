class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        if l == 1:
            return nums

        # nums = [2, 3, 4, 5]

        i = 1
        prefix = [0] * l
        prefix[0] = 1
        while i < l:
            prefix[i] = prefix[i-1] * nums [i-1]
            i += 1
        # prefix = [1, 2, 6, 24]

        i = l-2
        suffix = [0] * l
        suffix[l-1] = 1
        while i >= 0:
            suffix[i] = suffix[i+1] * nums[i+1]
            i -= 1
        # suffix = [60,20,5,1]

        res = [0] * l
        i = 0
        while i < l:
            res[i] = prefix[i] * suffix[i]
            i += 1

        return res
