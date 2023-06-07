import pytest

from ds.mono_stack import left_up, right_up, right_up_2


@pytest.mark.parametrize(
    ["sequence", "expected"],
    [
        ([], []),
        ([1, 3, 4, 2], [-1, -1, -1, 2]),
        ([1, 4, 3, 2], [-1, -1, 1, 2]),
        ([4, 1, 2, 3], [-1, 0, 0, 0]),
        ([1, 2, 2, 4], [-1, -1, -1, -1]),
    ],
)
def test_left_up(sequence: list[int], expected: list[int]) -> None:
    assert left_up(sequence) == expected


@pytest.mark.parametrize(
    ["sequence", "expected"],
    [
        ([], []),
        ([1, 3, 4, 2], [1, 2, -1, -1]),
        ([1, 4, 3, 2], [1, -1, -1, -1]),
        ([4, 1, 2, 3], [-1, 2, 3, -1]),
        ([1, 2, 2, 4], [1, 3, 3, -1]),
    ],
)
def test_right_up(sequence: list[int], expected: list[int]) -> None:
    assert right_up(sequence) == expected
    assert right_up_2(sequence) == expected
