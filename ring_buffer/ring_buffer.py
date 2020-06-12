# Node
class SinglyLinkedNode:
  def __init__(self, value, next_node=None):
    self._value = value
    self._next = next_node

  def get_value(self):
    return self._value

  def get_next(self):
    return self._next

  def set_next(self, next_node):
    self._next = next_node

# Linked List
class SinglyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def __len__(self):
    return self.length
    # length = 0
    # node = self.head
    # while node != None:
    #   length = length + 1
    #   node = node.get_next()
    # return length

  def get_head(self):
    return self.head
    
  def get_tail(self):
    return self.tail

  def append(self, value):
    node = SinglyLinkedNode(value)
    if self.head == None:
      self.head = node
      self.tail = node
    else:
      self.tail.set_next(node)
      self.tail = node
    self.length += 1

  def remove_last(self):
    last_node = self.tail
    if last_node == None:
      return None

    if self.head == last_node:
      self.head = None
      self.tail = None
    else:
      prev_to_last = self.head
      while not prev_to_last.get_next() == last_node:
        prev_to_last = prev_to_last.get_next()
      self.tail = prev_to_last
      self.tail.set_next(None)
    self.length -= 1
    return last_node.get_value()

  def remove_first(self):
    first_node = self.head
    if first_node == None:
      return None

    if self.tail == first_node:
      self.head = None
      self.tail = None
    else:
      self.head = self.head.get_next()
    self.length -= 1
    return first_node.get_value()

  def contains(self, data):
    node = self.head
    if self.head == None:
      return False
    while node != None:
      if node.get_value() == data:
        return True
      else:
        node = node.get_next()
    return False

  def get_max(self):
    if self.head == None:
      return None
    node = self.head
    max_value = node.get_value()
    while node.get_next() != None:
      node = node.get_next()
      if node.get_value() > max_value:
        max_value = node.get_value()
    return max_value

class LinkedList(SinglyLinkedList):

  def add_to_tail(self, data):
    super().append(data)

  def remove_tail(self):
    return super().remove_last()

  def remove_head(self):
    return super().remove_first()



class RingBufferArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.last = 0


    def append(self, item):
        if item != None and self.capacity > 0:
            if len(self.storage) == self.capacity:
                new_last = self.get_next()
                self.storage[new_last] = item
                self.last = new_last
                # self.next = self.get_next(self.next, self.capacity-1)
                # self.next = (self.next + 1) % (self.capacity)
            else:
                self.storage.append(item)
                # self.next = len(self.storage-1)

    def get(self):
        return self.storage

    def get_next(self):
        return (int(self.last)+1) % self.capacity


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = SinglyLinkedList()
        self.current = None

    def append(self, item):
        if self.capacity == 0:
            pass
        elif self.capacity > len(self.storage):
            self.storage.append(item)
            self.current = self.storage.tail
        else:
            if self.current == self.storage.tail:
                self.storage.head._value = item
                self.current = self.storage.head
            else:
                self.current._next.value = item
                self.current = self.current._next

    def get(self):
        node = self.storage.head
        result = []
        while node:
            result.append(node._value)
            node = node._next
        return result


import random
def test():
    buffer = RingBuffer(5)
    arr = ['a', 'b', 'c', 'd', 'd']
    for i in range(10):
        choice = random.randint(0, 4)
        print("adding: ", arr[choice])
        buffer.append(arr[choice])
        print(buffer.get())

test()