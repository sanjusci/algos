class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return '{}'.format(self.data)

    def __repr__(self):
        return self.__str__()


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        if self.isEmpty():
            node = Node(data)
            self.head = node
        else:
            node = self.head
            while node.next:
                node = node.next
            new_node = Node(data)
            node.next = new_node

    def appendRight(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def appendAfter(self, pos, data):
        tmp = self.head
        for i in range(pos):
            tmp = tmp.next
            if tmp is None:
                print("There are less than {} elements in list.".format(pos))
                break
        node = Node(data)
        node.next = tmp.next
        tmp.next = node

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
    lk = LinkedList()
    lk.append(14)
    lk.append(30)
    lk.append(25)
    lk.append(42)
    lk.append(17)
    lk.display()

    lk.appendRight(999)
    lk.appendRight(888)
    lk.appendRight(777)
    lk.display()

    lk.appendAfter(7, 0)
    lk.appendAfter(2, 1)
    lk.appendAfter(5, 99)
    lk.display()
    lk.count()

    lk.delete(99)
    lk.delete(1)
    lk.delete(10)
    lk.display()
    lk.display()
    lk.count()

