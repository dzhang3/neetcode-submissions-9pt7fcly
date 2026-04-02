class Twitter:

    def __init__(self):
        self.time = 0
        # holds each user's posts
        self.tweets = defaultdict(list) # (time,tweetId)
        # holds each user's feed using maxheap
        self.feeds = defaultdict(list)
        # holds each user's following
        self.following = defaultdict(set)
        # holds each user's followed by
        self.followers = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # add tweet to self storage and add to all followers feeds
        self.time +=1 
        self.tweets[userId].append((self.time,tweetId))
        
        for follower in self.followers[userId]:
            heapq.heappush_max(self.feeds[follower],(self.time,tweetId))          
        heapq.heappush_max(self.feeds[userId],(self.time,tweetId))    

    def getNewsFeed(self, userId: int) -> List[int]:
        # get first 10 of feed
        return [tweetId for _,tweetId in heapq.nlargest(10,self.feeds[userId])]

    def follow(self, followerId: int, followeeId: int) -> None:
        # add them to follower list and add their content to feed
        if followerId == followeeId or followeeId in self.following[followerId]:
            return
        for post in self.tweets[followeeId]:
            heapq.heappush_max(self.feeds[followerId],post)
        self.following[followerId].add(followeeId)
        self.followers[followeeId].add(followerId)
       

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # remove them from follower list and remove their content from feed
        if followerId == followeeId or followeeId not in self.following[followerId]:
            return
        self.following[followerId].remove(followeeId)
        self.followers[followeeId].remove(followerId)

        for post in self.tweets[followeeId]:
            self.feeds[followerId].remove(post)
        heapq.heapify_max(self.feeds[followerId])
