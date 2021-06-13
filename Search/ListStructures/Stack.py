class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def add(self, item):
        self.items.append(item)

    def remove(self):
        if self.isEmpty:
            raise Exception("Stack is empty.")
        else:
            out = self.items[-1]
            self.items = self.items[:-1]
            return out
    
    def __len__(self):
        return len(self.items)

if __name__ == "__main__":
    stack = Stack()
    for i in range(5):
        stack.add(i)
    print("Stack item sequence:")
    print(stack.items)
    print("Remove sequence")
    while not(stack.isEmpty):
        stack.remove()