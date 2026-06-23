"""Multiplication table utility module"""


def generate_multiplication_table(n, rows=10):
    """
    Generate a multiplication table for a given number.
    
    Args:
        n (int): The number to create a multiplication table for
        rows (int): Number of rows to generate (default: 10)
    
    Returns:
        list: List of strings representing the multiplication table
    """
    table = []
    for i in range(1, rows + 1):
        result = n * i
        table.append(f"{n} × {i} = {result}")
    return table


def print_multiplication_table(n, rows=10):
    """Print a multiplication table for a given number."""
    print(f"\nMultiplication Table for {n}:")
    print("-" * 25)
    for line in generate_multiplication_table(n, rows):
        print(line)


def create_full_table(n):
    """
    Create a full multiplication table (n × n).
    
    Args:
        n (int): Size of the table
    
    Returns:
        list: 2D list representing the multiplication table
    """
    table = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append(i * j)
        table.append(row)
    return table


def print_full_table(n):
    """Print a full multiplication table (n × n)."""
    print(f"\n{n} × {n} Multiplication Table:")
    print("-" * (n * 4 + 2))
    
    # Header
    print("  ", end="")
    for j in range(1, n + 1):
        print(f"{j:3}", end=" ")
    print()
    
    # Rows
    for i in range(1, n + 1):
        print(f"{i:2}", end=" ")
        for j in range(1, n + 1):
            print(f"{i*j:3}", end=" ")
        print()


if __name__ == "__main__":
    # Example usage
    print_multiplication_table(5, 10)
    print_full_table(10)
