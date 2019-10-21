

class Queue(object):

    MAX = 10

    def __init__(self):
        self.front = -1
        self.rear = -1
        self.head = [None] * self.MAX

    def add(self, data):
        if self.rear == self.MAX - 1:
            print("Queue is full!\n")
            return
        self.rear += 1
        self.head[self.rear] = data
        if self.front == -1:
            self.front = 0

    def delqueue(self) -> int:
        if self.front == -1:
            print("Queue is empty!")
            return
        data = self.head[self.front]
        self.head[self.front] = 0
        if self.front == self.rear:
            self.front, self.rear = -1, -1
        else:
            self.front += 1
        return data

    def display(self):
        que = self.head
        front = self.front
        print("\nDisplay Queue: ")
        while front <= self.rear:
            print(que[front])
            front += 1


if __name__ == '__main__':

    q = Queue()
    q.add(23)
    q.add(9)
    q.add(11)
    q.add(-10)
    q.add(25)
    q.add(16)
    q.add(17)
    q.add(22)
    q.add(19)
    q.add(30)
    q.add(32)

    q.display()

    i = q.delqueue()
    if i:
        print("Item popped: {}".format(i))
    i = q.delqueue()
    if i:
        print("Item popped: {}".format(i))
    i = q.delqueue()
    if i:
        print("Item popped: {}".format(i))
    q.display()
