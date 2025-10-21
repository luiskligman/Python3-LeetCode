class TimeMap:

    def __init__(self):
        self.TimeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.TimeMap:
            self.TimeMap[key] = []
        self.TimeMap[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.TimeMap:
            return res
        
        values = self.TimeMap[key]
        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2

            # We need to account for when the given timestamp is not stored within our values list
            # If the timestamp is not found, find the closest lesser value; this will be the leftmost value of the window
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else: 
                r = m - 1        
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
