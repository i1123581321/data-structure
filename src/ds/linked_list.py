from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Generic, Self, TypeVar

T = TypeVar("T")


@dataclass
class Node(Generic[T]):
    value: T
    next: Self | None = field(init=False, default=None)

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Node):
            if self.value != __value.value:
                return False
            if self.next is None:
                return __value.next is None
            return self.next == __value.next
        else:
            return False


def from_iterable(values: Iterable[T]) -> Node[T] | None:
    result: Node[T] | None = None
    p = None
    for value in values:
        if p is None:
            p = Node(value)
            result = p
        else:
            p.next = Node(value)
            p = p.next
    return result


def cut(node: Node[T] | None, n: int) -> tuple[Node[T] | None, int]:
    if n <= 0:
        raise ValueError()
    if node is None:
        raise ValueError()

    p: Node[T] | None = node
    length = 1
    for _ in range(n - 1):
        if p is not None:
            length += 1
            p = p.next
        else:
            break

    if p is None:
        # 链表长度小于 n
        return None, length - 1

    result = p.next
    p.next = None
    return result, length


def reverse(node: Node[T] | None) -> Node[T] | None:
    if node is None:
        return None
    if node.next is None:
        return node

    result = node
    p: Node[T] | None = node.next
    node.next = None
    while p:
        temp = p.next
        p.next = result
        result = p
        p = temp
    return result
