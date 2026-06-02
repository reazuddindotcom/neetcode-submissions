class Solution:
    def __init__(self):
        self.result = []
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.findSum(nums, 0, target, [])
        return self.result
        
    def findSum(self, nums: List[int], s: int, target: int, comb: List[int]) -> None:
        if target == 0:
            self.result.append(comb)
            return

        if target < 0 or s >= len(nums):
            return

        new_comb = list(comb)
        new_comb.append(nums[s])
        self.findSum(nums, s, target-nums[s], new_comb)

        self.findSum(nums, s+1, target, comb)