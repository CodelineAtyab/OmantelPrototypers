"""Multiplication table utility for from_alhawraa."""

from __future__ import annotations


def get_int_input(prompt: str, min_value: int | None = None) -> int:
    while True:
        raw_value = input(prompt).strip()
        if not raw_value:
            print("Input cannot be empty. Please enter a number.")
            continue

        if not raw_value.lstrip("+-").isdigit():
            print("Please enter a valid integer.")
            continue

        value = int(raw_value)
        if min_value is not None and value < min_value:
            print(f"Please enter a number greater than or equal to {min_value}.")
            continue

        return value


def format_multiplication_table(number: int, limit: int) -> list[str]:
    return [f"{number} x {i} = {number * i}" for i in range(1, limit + 1)]


def main() -> None:
    print("=== Multiplication Table Utility ===")
    number = get_int_input("Enter the number: ")
    limit = get_int_input("Enter the limit: ", min_value=1)

    print("\nResult:")
    for line in format_multiplication_table(number, limit):
        print(line)


if __name__ == "__main__":
    main()
