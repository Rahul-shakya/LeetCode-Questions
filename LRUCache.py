from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.hmap = {}
        self.cap = capacity
        self.q = deque()

    def get(self, key: int) -> int:
        if key in self.hmap:
            val = self.hmap[key]
            self.q.remove(key)
            self.q.append(key)
            return val
        else:
            return -1
            

    def put(self, key: int, value: int) -> None:
        if key not in self.hmap:
            if len(self.q) == self.cap:
                removed = self.q.popleft()
                del self.hmap[removed]
        else:
            self.q.remove(key)
        self.hmap[key] = value
        self.q.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
