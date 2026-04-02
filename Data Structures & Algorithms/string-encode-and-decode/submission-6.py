class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for string in strs:
            strlen = len(string)
            ans += "/{strlen}/{string}".format(strlen = strlen, string = string)
        # print(ans)
        return ans
        

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        fuck = 0
        while i < (len(s)):
            if (s[i] == '/'):
                readLength = ''
                curNum = i + 1
                while (s[curNum] != '/'):
                    readLength += s[curNum]
                    curNum += 1

                ans.append(s[curNum + 1:curNum + int(readLength) + 1])
                i = curNum + int(readLength) + 1
            else:
                print("error")
                return
        
        return ans
                
                

