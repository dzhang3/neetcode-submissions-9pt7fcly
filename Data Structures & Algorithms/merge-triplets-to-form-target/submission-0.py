class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        c1 = c2 = c3 = False
        for a,b,c in triplets:
            if a == target[0] and b <= target[1] and c <= target[2]:
                c1 = True
            if b == target[1] and a <= target[0] and c <= target[2]:
                c2 = True
            if c == target[2] and a <= target[0] and b <= target[1]:
                c3 = True
        return c1 and c2 and c3
                