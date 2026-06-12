class Solution:
    # Submitting just for recording the first version
    def myPow(self, x: float, n: int) -> float:
        y = self.pow(x, abs(n))
        if n < 0:
            return 1/y
        return y
    def pow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if x == 0:
            return 0.0

        y = self.myPow(x*x, n//2)
        if n%2:
            y *= x

        return y

