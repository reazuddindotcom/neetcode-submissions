class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ll = len(heights)
        start = 0
        end = ll - 1
        max_area = 0
        while start < end:
            max_area = max(max_area, ((end-start)*(min(heights[start], heights[end]))))
            if heights[start] < heights[end]:
                start += 1
            elif heights[end] < heights[start]:
                end -= 1
            else:
                start += 1

        return max_area

        # [1,7,2,5,12,3,500,500,7,8,4,7,3,6]
