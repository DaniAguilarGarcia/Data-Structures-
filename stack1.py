#stack clas which is going to initialize a Python list
class Stack():
    def __init__(self):
        self.items= []
#Push is a member ofi ts class , and item is going to be taken as an Argument  
#Item is being assigned to an empty list
#append is a buil in method that adds an item to the end of the list.
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def get_stack(self):
        return self.items

myStack = Stack()
myStack.push("DOG")
myStack.push("CAT")
print(myStack.get_stack())
myStack.push("COW")
print(myStack.get_stack())
myStack.pop()
print(myStack.get_stack())