# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================



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
