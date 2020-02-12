
class Queue:
    def __init__(self):
        self.container = []
    def enqueue(self,k):
        self.container.append(k)
    def dequeue(self):
        try:
            self.container.pop(0)
        except Exception:
            print('The Queue is empty')
    def peek(self):
        try:
            return self.container[0]
        except Exception:
            print('Null')
    def isEmpty(self):
        return self.container == 0
    def view(self):
        return self.container
