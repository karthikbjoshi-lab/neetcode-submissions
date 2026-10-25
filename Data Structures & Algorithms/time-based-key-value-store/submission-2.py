from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.store=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        i=0
        j=len(self.store[key])-1

        mid=0
        while i<=j:
            mid=(i+j)//2

            if self.store[key][mid][0]<=timestamp:
                i=mid+1

            else:
                j=mid-1

        if j==-1:
            return ""
        else:
            return self.store[key][j][1]
