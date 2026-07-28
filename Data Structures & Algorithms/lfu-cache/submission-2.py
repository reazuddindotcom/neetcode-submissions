class LFUCache:

    def __init__(self, capacity: int):
        self.ordered_set = OrderedDict()
        self.freq_map = OrderedDict() # defaultdict()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.ordered_set:
            self.freq_map[key] = self.freq_map[key]+1
            self.ordered_set.move_to_end(key)
            return self.ordered_set[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:        
        if self.capacity == 0:
            return
        if key in self.ordered_set:
            if self.ordered_set[key] == value:
                # k-v already exists
                self.freq_map[key] = self.freq_map[key]+1
                return
            self.freq_map[key] = 1
            self.ordered_set[key] = value
            self.ordered_set.move_to_end(key)
            return

        if len(self.ordered_set) == self.capacity:
            min_key = min(self.ordered_set, key=lambda k:self.freq_map[k])
            del self.ordered_set[min_key]
            del self.freq_map[min_key]

        self.ordered_set[key] = value
        self.freq_map[key] = 1

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)