"""
Multiplication Table Generator
A fancier CLI version with banners, input validation, and a summary.
"""


def print_banner():
    print("=" * 40)
    print("     ✨ MULTIPLICATION TABLE TOOL ✨")
    print("=" * 40)
    print()


def multiplication_table(number, limit):
    """Print a multiplication table for `number` from 1 to `limit`."""
    print("-" * 40)
    for i in range(1, limit + 1):
        result = number * i
        print(f"  {number} x {i:>2} = {result}")
    print("-" * 40)


def get_input():
    """Prompt the user and validate input. Returns (number, limit) or None."""
    try:
        number = int(input("Enter a number: "))
        limit = int(input("Enter a limit: "))

        if limit < 1:
            print("❌ Limit must be a positive whole number.")
            return None

        return number, limit

    except ValueError:
        print("❌ Invalid input! Please enter whole numbers only (e.g. 2 and 10).")
        return None


def main():
    print_banner()

    while True:
        result = get_input()
        if result is None:
            again = input("Try again? (y/n): ").strip().lower()
            if again != "y":
                break
            print()
            continue

        number, limit = result
        print()
        multiplication_table(number, limit)
        print()
        print(f"📊 Printed {limit} lines for the number {number}.")
        print()

        again = input("Generate another table? (y/n): ").strip().lower()
        print()
        if again != "y":
            break

    print("✅ Done! Thanks for using the Multiplication Table Tool.")


if __name__ == "__main__":
    main()
