class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        mask = 1
        N = 32
        for i in range(N):
            result = result | (((n & mask) >> i) << N-i-1)
            mask = mask << 1

        return result