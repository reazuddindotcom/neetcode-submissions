class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_to_idx = {}
        for i, v in enumerate(nums):
            val_to_idx[v] = i

        for i, v in enumerate(nums):
            diff = target - v
            if diff in val_to_idx and val_to_idx[diff] != i:
                return [i, val_to_idx[diff]]

        return []

        