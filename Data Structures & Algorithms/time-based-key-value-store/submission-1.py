class TimeMap:

    def __init__(self):
        self.hashset = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashset:
            self.hashset[key] = []
        
        self.hashset[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashset:
            return ""
        values = self.hashset[key]
        
        left = 0
        right = len(values) - 1
        results = ""

        while left <= right:
            mid = (left + right) // 2

            if values[mid][0] <= timestamp:
                results = values[mid][1]
                left = mid + 1
            else: 
                right = mid - 1
        return results
