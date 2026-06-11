class Solution:
    def isHappy(self, n: int) -> bool:
        # if in the set - false
        # if 1 - true
        # add to set
        # collect digits
        # get next number
        # loop

        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)

            next_n = 0
            while n:
                d = n%10
                n //=10
                next_n += (d*d)

            n = next_n

        return True

        