class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ll = len(piles)
        if not piles:
            return 0
        if h < ll:
            return -1

        min_s = 1
        max_s = max(piles)
        min_s_need = max_s
        while min_s <= max_s:
            mid = min_s + (max_s - min_s) // 2
            h_need = self.hoursNeeded(piles, mid)
            if h_need > h:
                min_s = mid + 1
            else:
                min_s_need = mid
                max_s = mid - 1

        return min_s_need

    def hoursNeeded(self, piles: List[int], speed: int) -> int:
        h = 0
        for i in range(len(piles)):
            h += math.ceil(float(piles[i])/speed)

        return h

        