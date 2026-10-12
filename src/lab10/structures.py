from collections import deque


class Stack:
    """Стек LIFO: последний добавленный элемент выходит первым."""

    def __init__(self):
        self._data = []

    def push(self, item) -> None:
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)


class Queue:
    """Очередь FIFO: первый добавленный элемент выходит первым."""

    def __init__(self):
        self._data = deque()

    def enqueue(self, item) -> None:
        self._data.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self._data.popleft()

    def peek(self):
        if self.is_empty():
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print("Stack peek:", stack.peek())
    print("Stack pop:", stack.pop())
    print("Stack len:", len(stack), "empty:", stack.is_empty())
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    print("Queue peek:", queue.peek())
    print("Queue dequeue:", queue.dequeue())
    print("Queue len:", len(queue), "empty:", queue.is_empty())
