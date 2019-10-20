class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return '{}'.format(self.data)

    def __repr__(self):
        return self.__str__()


class StackLinkedList(object):

    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def pop(self):
        if self.head is Node:
            print("Stack is empty!")
            return
        node = self.head
        data = node.data
        self.head = node.next
        return data

    def display(self):
        node = self.head
        print("\nDisplay Nodes: ")
        while node:
            print(node.data)
            node = node.next


if __name__ == '__main__':
    sl = StackLinkedList()
    sl.push(14)
    sl.push(-3)
    sl.push(18)
    sl.push(29)
    sl.push(31)
    sl.push(16)
    sl.display()
    i = sl.pop()
    if i:
        print("Item popped: {}".format(i))
    i = sl.pop()
    if i:
        print("Item popped: {}".format(i))
    i = sl.pop()
    if i:
        print("Item popped: {}".format(i))

