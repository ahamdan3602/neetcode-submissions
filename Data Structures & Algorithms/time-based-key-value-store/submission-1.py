class TimeMap:
   
    def __init__(self):
        self.mp = {}
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mp:
            self.mp[key] = []
        self.mp.get(key).append([timestamp, value])


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp:
            return ""

        val = self.mp[key]
        l, r = 0, len(val) - 1
        res = "" # Track the closest valid value

        while l <= r:
            mid = l + (r - l) // 2
            current_time = val[mid][0]
            
            if timestamp == current_time:
                return val[mid][1]
            elif current_time < timestamp:
                # This is a valid candidate! Save it, but keep searching right 
                # to see if there's a closer one.
                res = val[mid][1]
                l = mid + 1  
            else:
                # Time is too big, it's invalid. Search left.
                r = mid - 1  

        return res
