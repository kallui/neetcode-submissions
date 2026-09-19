class TimeMap:

    def __init__(self):
        self.mp = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mp:
            self.mp[key] = []
        self.mp[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        res = None
        if key in self.mp:
            entry = self.mp[key]
            l, r = 0, len(entry)-1
            
            while l <= r:
                mid = (l+r) // 2

                if entry[mid][0] == timestamp:
                    return entry[mid][1]
                elif entry[mid][0] < timestamp:
                    l = mid+1
                    res = entry[mid][1] # save the most recent prevTimestamp value
                elif entry[mid][0] > timestamp:
                    r = mid-1
        
        return res or ""
