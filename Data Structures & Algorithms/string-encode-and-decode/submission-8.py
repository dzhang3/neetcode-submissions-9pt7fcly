class Solution:

    def encode(self, strs: List[str]) -> str:
        # eg. number
        code = ""
        for s in strs:
            if len(s) == 0:
                code += "0:a/"
                continue
            start,end = 0,0
            while end < len(s):
                if s[start] != s[end]:
                    code += str(end - start) + ":" + s[start]
                    start = end
                end += 1
            code += str(end - start) + ":" + s[start] + "/"
        return code
        

    def decode(self, s: str) -> List[str]:
        ret = []
        start,end = 0,0
        cur = ""
        while end < len(s):
            while s[end].isdigit():
                end += 1
            # end now at colon
            end += 1
            # now at char
            # print(s,start,end,s[start],s[end])
            cur += int(s[start:end - 1]) * s[end]
            end += 1
            if s[end] == '/':
                # print("/ found, end:",end)
                ret.append(cur)
                cur = ""
                end += 1
            start = end
        return ret
