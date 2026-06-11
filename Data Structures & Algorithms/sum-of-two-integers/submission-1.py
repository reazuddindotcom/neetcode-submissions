class Solution:
    def getSum(self, a: int, b: int) -> int:
        N = 32
        c = 0
        result = 0
        for i in range(N):
            ai = (a >> i) & 1
            bi = (b >> i) & 1

            r, c = self.addBit(ai, bi, c)
            result |= (r << i)

        # 2's complement only needed in python
        if result > ((1<<31) - 1):
            result = ~ (result ^ (((1<<32) - 1)))


        return result
            

    def addBit(self, a: int, b: int, c: int) -> [int, int]:
        return [(a^b^c), ((a&b) | (a&c) | (b&c))] # Need a Fix to compute new carry