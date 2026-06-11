class Solution:
    def reverse(self, x: int) -> int:
        xx = abs(x)
        result = 0
        print(result, xx)
        while xx > 0:
            next_d = xx % 10
            result = result * 10 + next_d
            xx //= 10
            print(result, xx)

        if x < 0:
            result = -result

        if result > (2**31-1) or result < (-2**31):
            return 0

        return result