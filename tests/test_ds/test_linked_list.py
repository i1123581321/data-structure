import pytest

from ds.linked_list import Node, cut, from_iterable, reverse


@pytest.mark.parametrize(
    ["node", "n", "a", "b", "i"],
    [
        (
            from_iterable([1, 2, 3, 4]),
            1,
            from_iterable([1]),
            from_iterable([2, 3, 4]),
            1,
        ),
        (
            from_iterable([1, 2, 3, 4]),
            2,
            from_iterable([1, 2]),
            from_iterable([3, 4]),
            2,
        ),
        (
            from_iterable([1, 2, 3, 4]),
            3,
            from_iterable([1, 2, 3]),
            from_iterable([4]),
            3,
        ),
        (
            from_iterable([1, 2, 3, 4]),
            4,
            from_iterable([1, 2, 3, 4]),
            None,
            4,
        ),
        (
            from_iterable([1, 2, 3, 4]),
            5,
            from_iterable([1, 2, 3, 4]),
            None,
            4,
        ),
        (
            from_iterable([1, 2, 3, 4]),
            6,
            from_iterable([1, 2, 3, 4]),
            None,
            4,
        ),
    ],
)
def test_cut(
    node: Node[int] | None, n: int, a: Node[int] | None, b: Node[int] | None, i: int
) -> None:
    result, length = cut(node, n)
    assert node == a
    assert result == b
    assert length == i


@pytest.mark.parametrize(
    ["node", "n"], [(from_iterable([1, 2]), -1), (from_iterable([1, 2]), 0), (None, 1)]
)
def test_cut_raise(node: Node[int] | None, n: int) -> None:
    with pytest.raises(ValueError):
        cut(node, n)


@pytest.mark.parametrize(
    ["node", "expected"],
    [
        (from_iterable([]), from_iterable([])),
        (from_iterable([1]), from_iterable([1])),
        (from_iterable([1, 2]), from_iterable([2, 1])),
        (from_iterable([1, 2, 3]), from_iterable([3, 2, 1])),
    ],
)
def test_reverse(node: Node[int] | None, expected: Node[int] | None) -> None:
    assert reverse(node) == expected
