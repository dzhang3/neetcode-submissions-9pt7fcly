class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0 or n < groupSize:
            return False

        if groupSize == 1:
            return True

        counts = Counter(hand)

        for i in range(0,max(hand) + 1):
            if counts[i] > 0:
                c = counts[i]
                for j in range(groupSize):
                    if counts[i + j] < c:
                        return False
                    counts[i + j] -= c
                    # print(counts,i + j)
                # print(i,counts)
        return counts.total() == 0
