class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        cur = [[]]
        for i in nums:
            temp = list(cur)
            for subset in temp:
                new_set = list(subset)
                new_set.append(i)
                cur.append(new_set)

        return cur
