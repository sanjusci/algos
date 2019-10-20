class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return '{}'.format(self.data)

    def __repr__(self):
        return self.__str__()


class AscLinkedList(object):

    def __init__(self):
        self.head = None

    def add(self, data):
        node = self.head
        r = Node(data)
        if self.isEmpty() or self.head.data > data:
            self.head = r
            self.head.next = node
        else:
            while node:
                if node.data <= data and (node.next is None or node.next.data > data):
                    r.next = node.next
                    node.next = r
                    break
                node = node.next

    def reverse(self):
        node = self.head
        r = None
        while node:
            s = r
            r = node
            node = node.next
            r.next = s
        self.head = r

    def count(self):
        count = 0
        node = self.head
        while node:
            node = node.next
            count += 1
        print("\nNo of element in the Linked list {}".format(count))

    def delete(self, data):
        node = self.head
        old = None
        while node.next:
            if node.data == data:
                if node == self.head:
                    self.head = node.next
                else:
                    old.next = node.next
                return
            else:
                old = node
                node = node.next
        print("\nElement {} not found".format(data))

    def isEmpty(self):
        return not self.head

    def display(self):
        node = self.head
        print("\nDisplay Nodes: ")
        while node:
            print(node.data, end=" ")
            node = node.next


if __name__ == '__main__':
    lk = AscLinkedList()
    lk.add(5)
    lk.add(1)
    lk.add(6)
    lk.add(4)
    lk.add(7)
    lk.display()
    lk.count()
    lk.reverse()
    lk.display()

