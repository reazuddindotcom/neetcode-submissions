class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].pop(0) # Pop the earliest one, not the latest
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.follows[userId].add(userId)

        heap = []
        for followee in self.follows[userId]:
            tweets = self.tweets[followee]
            if not tweets:
                continue
            index = len(tweets) - 1
            # print(tweets)
            # print(index)
            tweet = tweets[index]
            heapq.heappush(heap, (-tweet[0], tweet[1], followee, index))

        feed = []
        i = 0
        while heap and i < 10:
            tweet = heapq.heappop(heap)
            feed.append(tweet[1])

            followee = tweet[2]
            idx = tweet[3]
            if idx > 0:
                idx -= 1 
                tweet = self.tweets[followee][idx]
                heapq.heappush(heap, (-tweet[0], tweet[1], followee, idx))

            i += 1

        return feed




    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # print("Unfollow: ", followerId, followeeId)
        # print(self.follows[followerId])
        # GOTCHA: unfollow can be called multiple times on the same pair
        self.follows[followerId].discard(followeeId)
        
