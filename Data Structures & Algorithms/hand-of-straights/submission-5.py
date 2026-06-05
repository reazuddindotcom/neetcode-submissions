class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if not hand or groupSize > len(hand):
            return False

        hand.sort()
        count_map = {}
        for i in hand:
            count_map[i] = count_map.get(i, 0) + 1

        hands = []
        l = len(hand)
        i = 0
        while i < l:
            hands.append(hand[i])
            while i < l and hands[-1] == hand[i]:
                i += 1
    
        l = len(hands)
        i = 1
        # while i < l:    # CONSIDER 1 2 3  51 52 53 
        #     if hands[i] -  hands[i-1] != 1:
        #         return False
        #     i += 1

        i = 0
        while i < l:
            j = i + 1
            while j < l and j < i + groupSize:    # CONSIDER 1 2 3  51 52 53 
                if hands[j] -  hands[j-1] != 1:
                    return False
                j += 1

            j = i
            min_val = float("inf")
            while j < l and j < i + groupSize:
                min_val = min(min_val, count_map[hands[j]])
                if count_map[hands[j]] == 0:
                    return False
                j += 1

            if j - i != groupSize:
                return False

            j = i
            new_start = j + groupSize
            while j < l and j < i + groupSize:
                count_map[hands[j]] = count_map[hands[j]] - min_val
                if count_map[hands[j]]:
                    new_start = min(new_start, j)
                j += 1
            
            i = new_start

        return i == l


# WA
# hand=[1,2,3,6,2,3,4,7,8]
# groupSize=3
# hand=[8,10,12]
# groupSize=3