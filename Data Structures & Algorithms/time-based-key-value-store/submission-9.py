class TimeMap:

    def __init__(self):
        self.mp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        li = self.mp[key]
        l, r = 0, len(li)-1

        res = ""
        while l <= r:
            m = (l+r) // 2
            val, tstamp = li[m]
            
            if tstamp <= timestamp:
                res = li[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return res
