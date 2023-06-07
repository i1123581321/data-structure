from collections.abc import Sequence
from typing import Any, TypeVar

T = TypeVar("T")


def left_up(seq: Sequence[Any]) -> list[int]:
    n = len(seq)
    if n == 0:
        return []
    stack: list[int] = []
    result: list[int] = [0] * n
    for i, a in enumerate(seq):
        while stack and seq[stack[-1]] <= a:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        else:
            result[i] = -1
        stack.append(i)
    return result


def right_up(seq: Sequence[Any]) -> list[int]:
    n = len(seq)
    if n == 0:
        return []
    stack: list[int] = []
    result: list[int] = [0] * n
    for i, a in reversed(list(enumerate(seq))):
        while stack and seq[stack[-1]] <= a:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        else:
            result[i] = -1
        stack.append(i)
    return result


def right_up_2(seq: Sequence[Any]) -> list[int]:
    n = len(seq)
    if n == 0:
        return []
    stack: list[int] = []
    result: list[int] = [0] * n
    for i, a in enumerate(seq):
        while stack and seq[stack[-1]] < a:
            temp = stack.pop()
            result[temp] = i
        stack.append(i)
    while stack:
        result[stack.pop()] = -1
    return result
