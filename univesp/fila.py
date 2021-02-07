class Fila():
    def __init__(self):
        self.data = []

    def inserir(self, item):
        self.data.append(item)

    def remover(self):
        if len(self.data) > 0:
            return self.data.pop(0)

    def top(self):
        if not self.isEmpty():
            return self.data[0]

    def isEmpty(self):
        return not len(self.data) > 0
