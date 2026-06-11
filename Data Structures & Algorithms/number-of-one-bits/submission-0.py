class Solution:
    def hammingWeight(self, n: int) -> int:
        mask = 1
        count = 0
        for i in range(32):
            if mask & n:
                count += 1
            mask = mask << 1
        
        return count