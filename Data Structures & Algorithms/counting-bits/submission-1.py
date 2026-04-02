class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(0,n+1):
            # print([1 if c == '1' else 0 for c in format(i,'b')])
            ans[i] = sum([1 if c == '1' else 0 for c in format(i,'b')])
        return ans
