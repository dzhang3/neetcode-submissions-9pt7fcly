class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0 or n < groupSize:
            return False

        if groupSize == 1:
            return True

        counts = Counter(hand)
        hand = sorted(hand)

        for i in hand:
            if counts[i] > 0:
                c = counts[i]
                for j in range(groupSize):
                    if counts[i + j] < c:
                        return False
                    counts[i + j] -= c
        return True
