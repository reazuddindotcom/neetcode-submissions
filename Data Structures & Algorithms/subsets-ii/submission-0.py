class Solution:
    def __init__(self):
        self.result = []
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        self.buildSubset(nums, 0, [])

        return self.result

    def buildSubset(self, nums: List[int], i: int, sub: List[int]) -> None:
        if i >= len(nums):
            self.result.append(list(sub))
            return

        sub.append(nums[i])
        self.buildSubset(nums, i+1, sub)
        sub.pop()

        while i < len(nums) - 1 and nums[i] == nums[i+1]:
            i += 1

        self.buildSubset(nums, i+1, sub)
        