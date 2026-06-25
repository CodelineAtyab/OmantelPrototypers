def generate_multiplication_table(number: int, limit: int) -> list[str]:
    """Build a multiplication table for a number up to the given limit."""
    if limit < 1:
        raise ValueError("Limit must be at least 1.")

    return [f"{number} x {count} = {number * count}" for count in range(1, limit + 1)]


def run_cli() -> int:
    """Run the interactive CLI multiplication-table app."""
    try:
        number = int(input("Enter the number: "))
        limit = int(input("Enter the limit: "))
        for line in generate_multiplication_table(number, limit):
            print(line)
    except ValueError as exc:
        print(f"Invalid input: {exc}")
        return 1

    print("Exiting Application!")
    return 0


if __name__ == "__main__":
    raise SystemExit(run_cli())