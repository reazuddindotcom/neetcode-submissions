class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0

        l1 = len(text1)
        l2 = len(text2)

        lcs = [[0] * (l2+1) for _ in range(l1+1)]

        # for i in range(l1):
        #     if text1[i] == text2[0]:
        #         lcs[i][0] = 1
        
        # for j in range(l2):
        #     if text2[j] == text1[0]:
        #         lcs[0][j] = 1

        for i in range(l1-1, -1, -1):
            for j in range(l2-1, -1, -1):
                if text1[i] == text2[j]:
                    lcs[i][j] = lcs[i+1][j+1] + 1
                else:
                    lcs[i][j] = max(lcs[i+1][j], lcs[i][j+1])


        return lcs[0][0]
