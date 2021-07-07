class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        node = Node(value)
        self.tail.next = node
        self.tail = node
        self.length += 1

    def _traverse(self, index):
        if index >= self.length: return self.tail
        if index <= 0: return self.head
        node = self.head
        for i in range(index-1):
            node = node.next
        return node

    def insert(self, value, index):
        new_node = Node(value)
        left_node = self._traverse(index)
        new_node.next = left_node.next
        left_node.next = new_node
        self.length += 1

    def delete(self, index):
        node = self._traverse(index + 1)
        if node == self.head:
            self.head = node.next
        else:
            left_node = self._traverse(index)
            left_node.next = node.next
        self.length -= 1

    def prepend(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1

    def display(self):
        llist = []
        node = self.head
        for index in range(self.length):
            print(node.value)
            llist.append(node.value)
            node = node.next
        return llist

    def reverse(self):
        first = self.head
        self.tail = first
        second = first.next
        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp
        self.head.next = None
        self.head = first

obj = LinkedList(12)
obj.append(24)
obj.append(48)
obj.prepend(6)
obj.insert(18, 2)
obj.insert(32, 4)
obj.insert(60, 99)
print(obj.display())
obj.delete(3)
print(obj.display())
obj.delete(0)
print(obj.display())
obj.reverse()
print(obj.display())
