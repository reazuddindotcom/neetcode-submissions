class TimeMap:

    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.keyStore:
            return ""

        return self.search(self.keyStore[key], timestamp)
        
    def search(self, values: list, timestamp: int) -> str:
        l = 0
        r = len(values) - 1

        while l <= r:
            m = l + (r - l) // 2
            if values[m][0] == timestamp:
                return values[m][1]

            if values[m][0] < timestamp:
                l = m + 1
            else:
                r = m - 1

        if r < 0:
            return ""
        else:
            return values[r][1]
