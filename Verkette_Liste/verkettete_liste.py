from __future__ import annotations

from dataclasses import dataclass
import random
from typing import Iterator, Optional


@dataclass
class Node:
    value: int
    next: Optional["Node"] = None


class SinglyLinkedList:

    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self._length: int = 0

    def append(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("nur int spast")

        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self._length += 1
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node
        self._length += 1

    def __len__(self) -> int:
        return self._length

    def __iter__(self) -> Iterator[int]:
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __str__(self) -> str:
        if self.head is None:
            return "[]"
        return "[" + " -> ".join(str(value) for value in self) + "]"

    def print_all(self) -> None:
        print("Alle Elemente:", ", ".join(str(value) for value in self) or "(leer)")


def main():
    linked_list = SinglyLinkedList()

    for _ in range(10):
        linked_list.append(random.randint(1, 100))

    print("Einfach verkettete Liste:", linked_list)
    print("Laenge der Liste:", len(linked_list))
    linked_list.print_all()

    print("Iteration ueber die Liste:")
    for value in linked_list:
        print(value)


if __name__ == "__main__":
    main()
