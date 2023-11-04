class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def get(self, index):
        if index < 0 or self.head is None:
            return None
        current = self.head
        for i in range(index):
            if current.next is None:
                return None
            current = current.next
        return current.data

    def remove(self, index):
        if index < 0 or self.head is None:
            return
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        for i in range(index - 1):
            if current.next is None:
                return
            current = current.next
        if current.next is None:
            return
        current.next = current.next.next

    def insert(self, n, val):
        if n < 0:
            return
        new_node = Node(val)
        if n == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for i in range(n - 1):
            if current.next is None:
                return
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next


ll = LinkedList()
ll.push(1)
ll.push(2)
ll.push(3)
ll.remove(1)
ll.insert(1, 4)

for item in ll:
    print(item)
