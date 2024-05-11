class TimeMap:

    def __init__(self):
        self.timeDict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeDict[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        timeList = self.timeDict[key]

        if not timeList:
            return ''
        left = 0
        right = len(timeList) - 1

        while(left <= right):
            mid = left + (right - left)//2

            if(timeList[mid][1] == timestamp):
                return timeList[mid][0]
            elif(timeList[mid][1] < timestamp):
                left = mid + 1
            else:
                right = mid - 1

        if timeList[right][1] > timestamp:
            return ''
        else:
            return timeList[right][0]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)