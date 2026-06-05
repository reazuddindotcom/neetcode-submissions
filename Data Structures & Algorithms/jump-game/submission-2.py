class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            True
        l = len(nums)
        # can_reach = [False]*l
        # can_reach[l-1] = True
        can_reach = True
        last = l-1
        for i in range(l-2, -1, -1):
            if i+nums[i] >= last:
                last = i
                can_reach = True
            else:
                can_reach = False

        return can_reach