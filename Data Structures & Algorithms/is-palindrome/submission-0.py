class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)
        if length <= 1:
            return True

        s = s.lower()
        end = length - 1
        start = 0
        while start < end:
            if not s[start].isalnum():
                start += 1
                # print("start")
                # print(start)
                continue
            if not s[end].isalnum():
                end -= 1
                # print("end")
                # print(end)
                continue

            if s[start] != s[end]:
                # print(s[start])
                # print(s[end])
                return False

            start += 1
            end -= 1

        return True