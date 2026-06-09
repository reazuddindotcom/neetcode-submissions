class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        l = len(nums)
        if l == 1:
            return nums[0]
        
        maxProd = 1
        minProd = 1
        max_res = nums[0]
        for n in nums:
            # if n == 0:
            #     maxProd = 1
            #     minProd = 1
            #     continue
            temp = maxProd
            maxProd = max(minProd * n, maxProd * n, n)
            minProd = min(minProd * n, temp * n, n)
            max_res = max(max_res, maxProd, minProd)

        return max_res