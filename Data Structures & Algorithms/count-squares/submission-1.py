class CountSquares:
    # are the squares always going to be aligned with
    # the axes ?

    def __init__(self):
        self.counts = {}

    def add(self, point: List[int]) -> None:
        self.counts[(point[0], point[1])] = self.counts.get((point[0], point[1]), 0) + 1

    def count(self, point: List[int]) -> int:
        count = 0
        print(self.counts)
        for p in self.counts:
            # avoid counting same point as the query point
            if p[0] != point[0] and abs(p[0]-point[0]) == abs(p[1]-point[1]):
                if (p[0],point[1]) in self.counts and (point[0], p[1]) in self.counts:
                    count += (self.counts[(p[0],p[1])] * self.counts[(p[0],point[1])] * self.counts[(point[0], p[1])])

        return count
        
# WA ["CountSquares", "add", [[5, 5]], "add", [[5, 6]], "add", [[6, 5]], "add", [[6, 6]], "count", [[7, 7]], "count", [[5, 5]]]
# Existing ["CountSquares", "add", [[1, 1]], "add", [[2, 2]], "add", [[1, 2]], "count", [[2, 1]], "count", [[3, 3]], "add", [[2, 2]], "count", [[2, 1]]]
