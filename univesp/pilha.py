class Pilha():
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pull(self):
        if not self.isEmpty():
            return self.data.pop(-1)

    def top(self):
        if not self.isEmpty():
            return self.data[-1]

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return len(self.data) == 0
