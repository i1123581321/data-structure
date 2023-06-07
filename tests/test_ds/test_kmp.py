import pytest

from ds.kmp import get_pmt, kmp


@pytest.mark.parametrize(
    ["s", "expected"], [("", []), ("ABCDABD", [0, 0, 0, 0, 1, 2, 0])]
)
def test_get_pmt(s: str, expected: list[int]) -> None:
    assert get_pmt(s) == expected


@pytest.mark.parametrize(
    ["s", "p", "expected"], [("BBC ABCDAB ABCDABCDABDE", "ABCDABD", [15])]
)
def test_kmp(s: str, p: str, expected: list[int]) -> None:
    assert kmp(s, p) == expected
