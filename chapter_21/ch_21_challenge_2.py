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

my_list = [1, 2, 3, 4, 5]

for number in my_list:
    my_stack.push(number)

reverse = []

for i in range(my_stack.size()):
    reverse.append(my_stack.pop())

print(reverse)
