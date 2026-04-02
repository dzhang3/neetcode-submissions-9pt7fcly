class MedianFinder:

    def __init__(self):
        self.half1 = [] # max heap
        self.half2 = [] # min heap

    def addNum(self, num: int) -> None:
        if self.half1 and num <= (self.half1[0] * -1):
            heapq.heappush(self.half1,num * -1)
        else:
            heapq.heappush(self.half2,num)
        while len(self.half2) > len(self.half1):
            heapq.heappush(self.half1, heapq.heappop(self.half2) * -1)
        while len(self.half2) < len(self.half1) - 1:
            heapq.heappush(self.half2, heapq.heappop(self.half1) * -1)

    def findMedian(self) -> float:
        if len(self.half1) == len(self.half2):
            return ((self.half1[0] * -1) + self.half2[0]) / 2
        else:
             return (self.half1[0] * -1)
