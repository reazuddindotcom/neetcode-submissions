class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        idx_map = defaultdict(lambda: [-1, -1])
        for i in range(len(s)):
            if s[i] not in idx_map:
                idx_map[s[i]][0] = i
            idx_map[s[i]][1] = i # always update end index
            # print("1", i)

        result = []
        cur_sz = 0
        i = 0
        while i < len(s):
            cur_sz = idx_map[s[i]][1] - idx_map[s[i]][0] + 1
            j = i+1
            while j < idx_map[s[i]][0] + cur_sz: # shouldn't overflow index
                cur_sz = max(cur_sz, idx_map[s[j]][1] - idx_map[s[i]][0] + 1)
                j += 1

            result.append(cur_sz)
            i = j
            # print("2", i, j)

        return result
                