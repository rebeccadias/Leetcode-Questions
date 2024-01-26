from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.hashmap=OrderedDict()

    def get(self, key: int) -> int:

        if key in self.hashmap:
            self.hashmap.move_to_end(key)
            return self.hashmap[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.hashmap:
            if len(self.hashmap)<self.capacity:
                self.hashmap[key]=value
            else:
                self.hashmap.popitem(0)
                self.hashmap[key]=value
        else:
            self.hashmap[key]=value
            self.hashmap.move_to_end(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

"""
Refer this for Ordered Dict : https://www.geeksforgeeks.org/ordereddict-in-python/#
"""
