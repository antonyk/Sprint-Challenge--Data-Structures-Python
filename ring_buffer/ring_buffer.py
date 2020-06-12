class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.next = 0


    def append(self, item):
        if item != None and self.capacity > 0:
            if len(self.storage) == self.capacity:
                self.storage[self.next] = item
                self.next = self.get_next(self.next, self.capacity-1)
                # self.next = (self.next + 1) % (self.capacity)
            else:
                self.storage.append(item)
                # self.next = len(self.storage-1)

    def get(self):
        return self.storage

    def get_next(self, current, ceiling):
        return (int(current)+1) % ceiling
