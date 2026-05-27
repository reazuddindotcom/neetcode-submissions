class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)
        counts1 = [0] * 26
        counts2 = [0] * 26

        for c in s1:
            # print(c, (ord(c) - ord('a')))
            counts1[ord(c) - ord('a')] += 1

        l, r = 0, 0
        while r < len2:
            # print(s2[r], (ord(s2[r]) - ord('a')))
            i = ord(s2[r]) - ord('a')
            counts2[i] += 1
            while l <= r and counts2[i] > counts1[i]:
                counts2[ord(s2[l]) - ord('a')] -= 1
                l += 1

            if (r-l+1) == len1:
                return True
            
            r += 1
        
        return False