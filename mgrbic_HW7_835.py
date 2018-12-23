class Stack:
    container = []
    def __str__(self):
        return str(Stack.container)
    
    def __len__(self):
        return len(Stack.container)
    
    def isEmpty(self):
        if len(self.container) == 0:
            return True
        else:
            return False

    def push(self, item):
        self.item = item
        Stack.container.append(item)

    def pop(self):
        return Stack.container.pop()

#test/main
#Another problem the UI told me to just attatch test code to file instead of shell
s = Stack()
s.push('plate 1')
s.push('plate 2')
s.push('plate 3')
print(s)
s.pop()
s.pop()
s.pop()
print(s.isEmpty())
