class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append([value,timestamp])

        
    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.dic[key]) - 1
        poz = -1

        while l <= r:
            m = (l + r) // 2
            
            if self.dic[key][m][1] <= timestamp:
                poz = m
                l = m + 1
            else:
                r = m - 1
        if poz > -1:
            return self.dic[key][poz][0]
        return ""
        
