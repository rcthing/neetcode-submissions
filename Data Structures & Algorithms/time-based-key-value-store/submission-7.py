class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append([value,timestamp])

        
    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.dic[key]) - 1
        prevl = 0
        if not self.dic[key] or self.dic[key][0][1] > timestamp:
            return ""

        while l <= r:
            m = (l + r) // 2
            if self.dic[key][m][1] == timestamp:
                return self.dic[key][m][0]
            
            if self.dic[key][m][1] < timestamp:
                l = m + 1
            else:
                r = m - 1
        return self.dic[key][m][0] if self.dic[key][m][1] < timestamp else self.dic[key][m-1][0]
        
