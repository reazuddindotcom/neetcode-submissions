class Solution:
    def __init__(self):
        self.result = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums, set(), [])

        return self.result
    
    def backtrack(self, nums: List[int], used: set, perm: List[int]) -> None:
        if len(perm) == len(nums):
            self.result.append(list(perm))
            return

        
        for n in nums:
            if n in used:
                continue

            used.add(n)
            perm.append(n)
            self.backtrack(nums, used, perm)
            used.remove(n)
            perm.pop()

