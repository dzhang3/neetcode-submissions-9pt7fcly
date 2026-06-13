class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [gas[i] - cost[i] for i in range(len(gas))]
        if sum(diff) < 0: return -1
        for i in range(len(diff)):
            s = 0
            for j in range(len(diff)):
                s += diff[(i + j) % len(diff)]
                if s < 0:
                    break
            if j == len(diff) - 1:
                return i
        return -1