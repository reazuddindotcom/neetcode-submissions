class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # BFS with beginWord
        # for every word popped, find and push one-char-off words to queue
        # keep track of used words in a hash set
        used = set()
        pq = []
        heapq.heappush(pq, (1, beginWord))
        used.add(beginWord)
        while pq:
            d, w = heapq.heappop(pq)
            if w == endWord:
                return d

            for c_w in wordList:
                if c_w in used or not self.dist1(w, c_w):
                    continue
                used.add(c_w)
                heapq.heappush(pq, (d+1, c_w))

        return 0
                

    def dist1(self, w1: str, w2: str) -> bool:
        if len(w1) != len(w2):
            return 100

        d = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                d += 1
            if d == 2:
                return False

        return True




        