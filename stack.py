'''
Implementation of stack using list in python
'''

class EmptyStackException(Exception):
    def __init__(self):
        print("Stack is empty.")


class Stack():
    def __init__(self, item=None):
        self.items = list()
        if item:
            self.items.append(item)

    def add(self, item):
        '''
        add element/item on the top of the stack
        '''
        self.items.append(item)

    def remove(self):
        '''
        remove item from top of the stack
        '''
        if self.size() <= 0:
            raise EmptyStackException()
        self.items.pop()

    def size(self):
        return len(self.items)

    def __str__(self):
        '''
        print the items of stack from top to bottom
        '''
        return "\n".join(str(x) for x in self.items[::-1])


#stack = Stack()
stack = Stack(10)
#stack.remove()
stack.add(4)
stack.add(6)
stack.add(1)
print(stack.size())
stack.remove()
print(stack)