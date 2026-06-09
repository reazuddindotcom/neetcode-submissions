class Solution:
    def numDecodings(self, s: str) -> int:
        l = len(s)
        if l == 0:
            return 0

        num = [0] * l
        if self.isValid(s[0]):
            num[0] = 1
        if l == 1:
            return num[0]

        if self.isValid(s[0]) and self.isValid(s[1]):
            num[1] = 1
        if self.isValid(s[0:2]):
            num[1] += 1
        # 12 --> 2, 10 --> 1, 01 --> 0, 00 -> 0
        if l == 2:
            return num[1]


        for i in range(2, l, 1):
            if self.isValid(s[i]):
                num[i] = num[i-1]
            if self.isValid(s[i-1:i+1]):
                num[i] += num[i-2]
                # Take an example
            print(i)
            print(num)

        return num[l-1]

        
    def isValid(self, s: str) -> bool:
        i = int(s)
        if i < 1 or i > 26:
            return False

        if i < 10 and len(s) == 2:
            return False

        return True