

def print_multiplication_table(number):
    print(f"Multiplication Table for {number}:")
    for multiplier in range(1, 13):
        product = number * multiplier
        print(f"{number} x {multiplier:2} = {product}")


def print_tables_up_to(number):
    for current_number in range(1, number + 1):
        print_multiplication_table(current_number)
        if current_number < number:
            print("---------------------------")


def main():
    try:
        number = int(input("Enter a number for a single table: "))
    except ValueError:
        print("Error: Please enter a whole number.")
        return

    print_multiplication_table(number)

    try:
        last_table = int(input("\nEnter N for tables from 1 to N: "))
    except ValueError:
        print("Error: Please enter a positive integer.")
        return

    if last_table <= 0:
        print("Error: N must be a positive integer.")
        return

    print()
    print_tables_up_to(last_table)


if __name__ == "__main__":
    main()
