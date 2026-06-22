"""A simple CLI multiplication table utility."""

from __future__ import annotations


def get_int_input(prompt: str, min_value: int | None = None) -> int:
    while True:
        try:
            value = int(input(prompt).strip())
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if min_value is not None and value < min_value:
            print(f"Please enter a number greater than or equal to {min_value}.")
            continue

        return value


def format_multiplication_table(base: int, limit: int) -> list[str]:
    return [f"{base} x {i} = {base * i}" for i in range(1, limit + 1)]


def run_cli() -> None:
    print("Multiplication Table Utility")
    print("Enter a number and a limit to generate the table.")

    base = get_int_input("Number: ")
    limit = get_int_input("Limit: ", min_value=1)

    print("\nResult:")
    for line in format_multiplication_table(base, limit):
        print(line)


if __name__ == "__main__":
    run_cli()
