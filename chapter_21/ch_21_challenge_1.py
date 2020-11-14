class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items)-1
        return self.items[last]

    def size(self):
        return len(self.items)


my_stack = Stack()

for letter in 'yesterday':
    my_stack.push(letter)

reverse = ''

for i in range(my_stack.size()):
    reverse += my_stack.pop()

print(reverse)
