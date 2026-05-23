class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ll = len(numbers)
        start = 0
        end = ll - 1
        while start < end:
            summ = numbers[start] + numbers[end]
            if summ == target:
                return [start+1, end+1]
            if summ < target:
                start += 1
                continue
            if summ > target:
                end -= 1