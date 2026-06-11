class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            res.append(self.countBitsOfN(i))

        return res
        
    def countBitsOfN(self, n: int) -> int:
        mask = 1
        count = 0
        for i in range(32):
            if mask & n:
                count += 1
            mask = mask << 1
        
        return count