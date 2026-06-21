def generate_table(number, limit):
    for i in range(1, limit + 1):
        print(f"{number} x {i} = {number * i}")


def main():
    try:
        number = int(input("Enter a number: "))
        limit = int(input("Enter the limit: "))

        if limit <= 0:
            print("Limit must be greater than 0")
        else:
            generate_table(number, limit)

    except ValueError:
        print("Please enter valid integers only.")


if __name__ == "__main__":
    main()


    