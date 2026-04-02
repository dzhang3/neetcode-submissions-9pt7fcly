class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1freqs = [0] * 26
        s2freqs = [0] * 26

        for s in s1:
            s1freqs[ord(s) - ord('a')] += 1

        l,r = 0,0
        while r < len(s2):
            s2freqs[ord(s2[r]) - ord('a')] += 1
            while r - l + 1 > len(s1) or s2freqs[ord(s2[r]) - ord('a')] > s1freqs[ord(s2[r]) - ord('a')]:
                s2freqs[ord(s2[l]) - ord('a')] -= 1
                l += 1
            if r - l + 1 == len(s1):
                print(l,r)
                return True
            r += 1
        return False