import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from multi import get_multiplication_table


def test_get_multiplication_table_basic():
    expected = [
        "2 x 1 = 2",
        "2 x 2 = 4",
        "2 x 3 = 6",
    ]
    assert get_multiplication_table(2, 3) == expected


def test_get_multiplication_table_zero_limit():
    assert get_multiplication_table(5, 0) == []


def test_get_multiplication_table_negative_limit():
    assert get_multiplication_table(4, -1) == []


if __name__ == "__main__":
    test_get_multiplication_table_basic()
    test_get_multiplication_table_zero_limit()
    test_get_multiplication_table_negative_limit()
    print("All tests passed.")
