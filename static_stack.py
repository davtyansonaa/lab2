class stack():
    def __init__(self, maxsize):
        self.items=[]
        self.maxsize=maxsize
    def size(self):
        return len(self.items)
    def push(self,item):
        if self.size() >= self.maxsize:
            print("Stack overflow")
            return
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return 0 if self.items==[] else 1
    def top(self):
      print(self.items[-1])
    def is_full(self):
      if self.maxsize<=len(self.items):
        return 1
      else:
        return 0



stack1=stack(3)
for _ in range(5):
  stack1.push(3)

stack1.top()
