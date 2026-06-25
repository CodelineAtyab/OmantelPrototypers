def get_multiplication_table(number: int, limit: int) -> list[str]:
    """
    Return spacing-safe multiplication table lines for the given number and limit.
    """
    return [f"{number} x {i} = {number * i}" for i in range(1, limit + 1)]


def main() -> None:
    print("Multiplication Table Utility")
    print("Enter a number and a limit to generate the table.")

    try:
        number = int(input("Number: ").strip())
        limit = int(input("Limit: ").strip())
    except ValueError:
        print("Please enter valid integer values.")
        return

    for line in get_multiplication_table(number, limit):
        print(line)


if __name__ == "__main__":
    main()
