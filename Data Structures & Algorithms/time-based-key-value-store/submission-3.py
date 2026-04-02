from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.tm = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tm[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.tm.get(key,[])
        ret = ""
        l,r = 0,len(vals) - 1
        while l <= r:
            m = (l + r) // 2
            v,t = vals[m]
            if t <= timestamp:
                ret = v
                l = m + 1
            else:
                r = m - 1
        return ret
            
        
