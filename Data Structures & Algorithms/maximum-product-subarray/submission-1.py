class Solution:
    # [2,4,3,5]
    # [2,8,24,120]
    # 0 --> start over / split
    # 0 > all negative
    # [2,4,-3,5,-1]
    # 2,8,-24,-120,120
    # Prop: only reset when 0
    # Otherwise keep tracking min and max at each element
    # Finally, take the max of min, max arrays
    # No?
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
            tempMax = maxProd
            maxProd = max(minProd * n, tempMax * n, n)
            minProd = min(minProd * n, tempMax * n, n)
            max_res = max(max_res, maxProd, minProd)

        return max_res