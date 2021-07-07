class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top.value

    def pop(self):
        if not self.length == 0:
            result = self.top.value
            self.top = self.top.next
            self.length -= 1
            return result
        else:
            #TODO: return actual exception class object
            self.bottom == None
            return 'StackOverflowException'

    def push(self, value):
        if self.length == 0:
            self.top = self.bottom = Node(value)
        else:
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node
        self.length += 1


    def is_empty(self):
        return self.top == self.bottom

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

s = Stack()
s.push('google')
s.push('udemy')
s.push('stackoverflow')
print(s.peek())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
s.push('king')
print(s.pop())
print(s.pop())
print(s.is_empty())
