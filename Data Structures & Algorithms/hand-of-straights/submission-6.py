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
            if counts[i]:
                # print(i,counts[i])
                # c = counts[i]
                for j in range(i,i+groupSize):
                    if not counts[j]:
                        return False
                    counts[j] -= 1
        return True
