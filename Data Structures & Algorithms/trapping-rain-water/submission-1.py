class Solution:
    def trap(self, height: List[int]) -> int:
        # MY NAIVE SOLUTION
        # ll = len(height)
        # left_max = [0] * ll
        # right_max = [0] * ll

        # for i in range(1, ll, 1):
        #     left_max[i] = max(height[i - 1], left_max[i - 1])

        # for i in range(ll - 2, -1, -1):
        #     right_max[i] = max(height[i + 1], right_max[i + 1])

        # water = 0
        # for i in range(ll):
        #     w = min(left_max[i], right_max[i]) - height[i]
        #     if w < 0: # WHY IS THIS NOT NEEDED ???
        #         w = 0
        #     water += w

        # return water

        # LEARNING: For stack solution, tracking by index is important.
        # ??? WHY DOES THE STACK SOLUTION NEED TO CALCULATE AREA?

        # PROPOSED TWO POINTER SOLUTION
        ll = len(height)
        if ll <= 2:
            return 0
        
        left_max = height[0]
        right_max = height[ll-1]
        l = 1
        r = ll-2
        water = 0
        while l <= r:
            if left_max <= right_max:
                water += max(0, left_max - height[l])
                left_max = max(left_max, height[l])
                l += 1
            else:
                water += max(0, right_max - height[r])
                right_max = max(right_max, height[r])
                r -= 1

        return water