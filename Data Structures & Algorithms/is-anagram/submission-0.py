class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sc = Counter(s)
        tc = Counter(t)
        for k in sc.keys():
            if sc[k] != tc[k]:
                return False
        return True

