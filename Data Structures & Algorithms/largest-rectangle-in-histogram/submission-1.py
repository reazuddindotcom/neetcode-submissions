class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ll = len(heights)

        forward = [0] * ll
        stack = []
        for i in range(ll):
            l = 0
            # print(i)
            while stack and heights[i] < stack[-1][1]:
                pair = stack.pop()
                forward[pair[0]] = i - pair[0] - 1
                # print(pair[0])
                # print(pair[1])
                # print(forward[pair[0]])
                # print("--------------")
            # print("===============")

            stack.append((i, heights[i]))

        l = 0
        while stack:
            pair = stack.pop()
            forward[pair[0]] = l
            l += 1

        
        # [7,1,7,2,2,4]
        backward = [0] * ll
        stack = []
        for i in range(ll-1, -1, -1):

            while stack and heights[i] < stack[-1][1]:
                pair = stack.pop()
                backward[pair[0]] = pair[0] - i - 1

            stack.append((i, heights[i]))

        l = 0
        while stack:
            pair = stack.pop()
            backward[pair[0]] = l
            l += 1

        max_area = 0
        for i in range(ll):
            max_area = max(max_area, (heights[i] * (1 + forward[i] + backward[i])))
            # print(heights[i])
            # print(forward[i])
            # print(backward[i])
            # print(max_area)
            # print("---------")

        return max_area



        