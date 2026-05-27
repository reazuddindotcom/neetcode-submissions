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
        if not s:
            return

        freq = [0] * 26
        l, r = 0, 0
        max_l = 0
        maxf = 0

        while r < len(s):
            i = ord(s[r]) - ord('A')
            freq[i] += 1
            maxf = max(maxf, freq[i])
            # print(freq)
            # print(s[r], freq[i], maxf)
            while l < r and (r-l+1) - maxf > k:
                freq[ord(s[l])-ord('A')] -= 1
                l += 1
                maxf = max(freq)

            max_l = max(max_l, (r-l+1))
            r += 1

        return max_l


        