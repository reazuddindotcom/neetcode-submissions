class Solution:
    def __init__(self):
        self.result = []
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        self.findSum(candidates, 0, target, [])

        return self.result

    def findSum(self, nums: List[int], s: int, target: int, comb: List[int]) -> None:
        if target == 0:
            self.result.append(comb)
            return

        if target < 0 or s >= len(nums):
            return

        new_comb = list(comb)
        new_comb.append(nums[s])
        self.findSum(nums, s+1, target-nums[s], new_comb)


        while s < len(nums)-1 and nums[s] == nums[s+1]:
            s += 1
        # skip the current element
        self.findSum(nums, s+1, target, comb)
