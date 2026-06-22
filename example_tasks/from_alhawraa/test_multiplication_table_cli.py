import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from multiplication_table_cli import format_multiplication_table


def test_format_multiplication_table_basic() -> None:
    assert format_multiplication_table(2, 3) == [
        "2 x 1 = 2",
        "2 x 2 = 4",
        "2 x 3 = 6",
    ]


def test_format_multiplication_table_zero_limit() -> None:
    assert format_multiplication_table(5, 0) == []


def test_format_multiplication_table_negative_limit() -> None:
    assert format_multiplication_table(4, -1) == []


if __name__ == "__main__":
    test_format_multiplication_table_basic()
    test_format_multiplication_table_zero_limit()
    test_format_multiplication_table_negative_limit()
    print("All tests passed.")
