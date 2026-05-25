class Solution:
    def trap(self, height: List[int]) -> int:
        ll = len(height)
        left_max = [0] * ll
        right_max = [0] * ll

        for i in range(1, ll, 1):
            left_max[i] = max(height[i - 1], left_max[i - 1])

        for i in range(ll - 2, -1, -1):
            right_max[i] = max(height[i + 1], right_max[i + 1])

        water = 0
        for i in range(ll):
            w = min(left_max[i], right_max[i]) - height[i]
            if w < 0:
                w = 0
            water += w

        return water
