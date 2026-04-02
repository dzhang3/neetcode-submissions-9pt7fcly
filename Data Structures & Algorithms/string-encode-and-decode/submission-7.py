class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for s in strs:
            code += str(len(s)) + "%" + s
        return code

    def decode(self, s: str) -> List[str]:
        i = 0
        strs = []
        while i < len(s):
            num = ''
            while s[i] != '%':
                num += s[i]
                i += 1
            num = int(num)
            i += 1
            strs.append(s[i:i+num])
            i += num
        return strs

            
