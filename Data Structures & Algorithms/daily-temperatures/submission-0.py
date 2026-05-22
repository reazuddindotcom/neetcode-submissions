class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)
        for i,t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                tupl = stack.pop()
                result[tupl[1]] = i - tupl[1]

            stack.append((t, i))

        return result


         



# S: 40,5 28,6
# i: 0   1   2   3   4   5   6
# R: 1   4   1   2   1   0   0