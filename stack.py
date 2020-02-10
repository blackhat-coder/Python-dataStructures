
class Stack:

    def __init__(self):
        self.container = []
    
    def push(self, k):
        self.container.append(k)
    
    def pop(self):
        try:
            self.container.pop(len(self.container)-1)
        except Exception:
            print('They are no more items in the stack')
    
    def view_last(self):
        print(self.container[len(self.container) - 1])
    
    def length(self):
        print(len(self.container))
    
    def view_stack(self):
        return self.container
    
    def isEmpty(self):
        if len(self.container) == 0:
            return True
        else:
            return False
    
