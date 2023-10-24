# task2
class Node:
    """
    Вспомогательный класс для узлов списка
    """

    def __init__(self, data):
        self.data = data  # храним информацию
        self.next = None  # ссылка на следующий узел
        self.pref = None  # Ссылка на предыдущий узел


class Queue:
    """
    Основной класс
    """

    def __init__(self):
        self.head = None  # ссылка на начало очереди
        self.last = None  # ссылка на конец очереди

    def pop(self):
        """
        возвращаем элемент val из начала списка с удалением из списка
        """
        if self.head is None:
            return None
        else:
            temp = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return temp

    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        if self.last is None:
            self.head = Node(val)
            self.last = self.head
        else:
            self.last.next = None(val)
            self.last.next.prev = self.last
            self.last = self.last.next
        pass

    def insert(self, n, val):
        """
        вставить элемент val между элементами с номерами n-1 и n
        """
        if n == 0:
            new_node = Node(val)
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
        else:
            current = self.head
            index = 0
            while current is not None and index < n - 1:
                current = current.next
                index += 1
            if current is None:
                return
            new_node = Node(val)
            new_node.prev = current
            new_node.next = current.next
            if current.next:
                current.next.prev = new_node
            current.next = new_node

    def print(self):
        """
        вывод на печать содержимого очереди
        """
        temp = self.head
        while temp is not None:
            print(temp.data, end="->")
            temp = temp.next
