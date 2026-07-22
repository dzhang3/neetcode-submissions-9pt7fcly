class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAN(c):
            return ((ord(c) >= ord('a') and ord(c) <= ord('z'))
            or (ord(c) >= ord('A') and ord(c) <= ord('Z'))
            or (ord(c) >= ord('0') and ord(c) <= ord('9'))
            )

        i,j = 0,len(s) - 1
        while i < j:
            if not isAN(s[i]):
                i += 1
            elif not isAN(s[j]):
                j -= 1
            elif s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        return True
