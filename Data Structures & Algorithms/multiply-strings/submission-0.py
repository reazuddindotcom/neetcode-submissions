class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # the final result in int
        # cur_result for every iteration
        # result = result * 10 + cur_result : every iteration

        if not num1:
            return num2
        if not num2:
            return num1
        if num1 == "0" or num2 == "0":
            return "0"

        num1 = num1[::-1]
        num2 = num2[::-1]

        l1 = len(num1)
        l2 = len(num2)
        # Using int array for handling the addition
        result = [0] * (l1+l2)

        carry = 0
        i = 0
        while i < l1:
            d1 = int(num1[i])
            # print("i,d1",i,d1)
            j = 0
            while j < l2:
                d2 = int(num2[j])
                # print("j,d2",j,d2)
                # print("i+j", i+j, d1, d2, carry)
                r = d1 * d2 + carry
                # print("r", r)
                # print("r, carry", r, carry)
                result[i+j] += (r%10)
                # print("result[i+j]", result[i+j])
                carry = r//10 + result[i+j]//10
                # print("carry", carry)
                result[i+j] = result[i+j]%10
                # print("result[i+j]", result[i+j])
                j += 1
            if carry:
                result[i+j] += carry
                carry = 0
            i += 1
            # print(result)
            # print("----")

        j = l1+l2-1
        while j >=0 and result[j] == 0:
            j -= 1

        s = ""
        while j >= 0:
            s = s + str(result[j])
            j -= 1

        return s

