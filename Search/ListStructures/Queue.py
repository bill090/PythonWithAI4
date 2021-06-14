class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def add(self, item):
        self.items.append(item)

    def remove(self):
        if self.isEmpty():
            raise Exception("Stack is empty.")
        else:
            out = self.items[0]
            self.items = self.items[1:]
            return out
    
    def __len__(self):
        return len(self.items)

if __name__ == "__main__":
    queue = Queue()
    for i in range(5):
        queue.add(i)
    print("Stack item sequence:")
    print(queue.items)
    print("Remove sequence:")
    while not(queue.isEmpty()):
        print(queue.remove())