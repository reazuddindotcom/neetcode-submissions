class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position:
            return 0
        # Ask: Equal length guaranteed? 

        pairs = []
        for p, s in zip(position, speed):
            pairs.append((p,s))
        
        pairs.sort()
        ttr = []
        for p,s in pairs:
            ttr.append(float(target-p)/float(s)) # Is 'float' needed??

        length = len(ttr)
        fleets = 1
        arrival_t = ttr[length-1]
        for i in range(length-2, -1, -1):
            if ttr[i] <= arrival_t:
                continue
            arrival_t = ttr[i]
            fleets += 1
        
        return fleets


# 10
# [4,1,0,7]
# [2,2,1,1]
# Sort
# [0 1 4 7]
# [1 2 2 1]
# 10, 4.5, 3, 3