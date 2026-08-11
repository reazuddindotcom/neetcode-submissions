class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Q: k characters don't have to be contiguous
        # Obs: replacing the most frequent character won't
        # necessarily result in to the longest substring
        # Example: aacde
        # Do I need both map (to get/inc current freq) and
        # PQ (to bubble top frequencies)
        # What if just track repl_req? No aacde.
        # Easier Soln: Loop for each char :/
        # Based on the vedio, the optimum one (constant max lookup/update)
        # is very hard to get to. Rather use the fact that there are only
        # 26 characters. So look up max everytime. Still O(n).
        # The example code look much simpler
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            # GIVEN:: REPLACING WHILE WITH IF
            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res


        