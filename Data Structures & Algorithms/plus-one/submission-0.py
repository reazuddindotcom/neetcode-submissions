class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Can I modify the array in-place
        for i in range(len(digits)-1, -1, -1):
            a = (digits[i]+1)%10
            c = (digits[i]+1)//10

            digits[i] = a

            print(c, digits)
            if not c:
                break


        result = digits
        if c:
            result = [1, *digits]

        return result

        