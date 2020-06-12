class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            # new node becomes head of list
            # set current head's prev to new node
            new_node.next = self.head
            # set new node's next to current head
            self.head.prev = new_node
            # reassign self.head to point to the new node
            self.head = new_node

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.oldest = None
        self.dll = DoublyLinkedList()

    def append(self, item):
        if len(self.dll) == self.capacity:
            if self.oldest is None:
                    self.oldest = self.dll.tail
            self.oldest.value = item
            self.oldest = self.oldest.prev
        else:
            self.dll.add_to_head(item)
        

    def get(self):
        buffer_list = []
        node = self.dll.tail
        while node is not None:
          buffer_list += [node.value]
          node = node.prev
        return buffer_list
            