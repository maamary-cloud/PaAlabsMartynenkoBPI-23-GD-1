from collections import deque
from time import perf_counter
from src.lab10.linked_list import SinglyLinkedList


def main():
    n = 5000
    start = perf_counter()
    values = list(range(n))
    while values:
        values.pop(0)
    print(f"list: создание + pop(0), N={n}: {perf_counter() - start:.6f} с")
    start = perf_counter()
    values = deque(range(n))
    while values:
        values.popleft()
    print(f"deque: создание + popleft, N={n}: {perf_counter() - start:.6f} с")
    start = perf_counter()
    values = SinglyLinkedList()
    for i in range(n):
        values.append(i)
    print(f"Связный список: append без tail, N={n}: {perf_counter() - start:.6f} с")
    start = perf_counter()
    values = SinglyLinkedList()
    for i in range(n):
        values.prepend(i)
    print(f"Связный список: prepend, N={n}: {perf_counter() - start:.6f} с")


if __name__ == "__main__":
    main()
