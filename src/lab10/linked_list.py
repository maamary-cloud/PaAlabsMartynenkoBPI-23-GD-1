class Node:
    """Узел: значение и ссылка на следующий узел."""

    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    """Односвязный список без хвоста; append проходит весь список."""

    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, value) -> None:
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
        self._size += 1

    def prepend(self, value) -> None:
        node = Node(value)
        node.next = self.head
        self.head = node
        self._size += 1

    def insert(self, idx: int, value) -> None:
        if idx < 0 or idx > self._size:
            raise IndexError("Индекс вне списка")
        if idx == 0:
            self.prepend(value)
            return
        current = self.head
        for i in range(idx - 1):
            current = current.next
        node = Node(value)
        node.next = current.next
        current.next = node
        self._size += 1

    def remove(self, value) -> None:
        """Удаляет первое вхождение. Если значения нет — ValueError."""
        previous = None
        current = self.head
        while current is not None:
            if current.value == value:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                self._size -= 1
                return
            previous = current
            current = current.next
        raise ValueError("Значение не найдено")

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        return f"SinglyLinkedList({list(self)})"


if __name__ == "__main__":
    linked = SinglyLinkedList()
    linked.append(2)
    linked.prepend(1)
    linked.insert(2, 3)
    print(linked)
    linked.remove(2)
    print("После удаления:", linked)
    print("Перебор:", list(linked), "Длина:", len(linked))
