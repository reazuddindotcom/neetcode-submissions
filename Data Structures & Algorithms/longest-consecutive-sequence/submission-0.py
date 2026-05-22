class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        lcs_len = 0
        for n in nums:
            if n-1 not in num_set:
                cur_len = 0
                curr = n
                while curr in num_set:
                    curr += 1
                    cur_len += 1

                lcs_len = max(cur_len, lcs_len)

        return lcs_len