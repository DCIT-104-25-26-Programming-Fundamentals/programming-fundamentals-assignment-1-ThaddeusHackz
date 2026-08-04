# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================



def read_matrix(rows, columns, name):
    matrix = []
    print(f"Enter the values for matrix {name}:")

    for row_number in range(1, rows + 1):
        while True:
            row_input = input(f"Enter row {row_number}: ").split()

            if len(row_input) != columns:
                print(f"Error: Enter exactly {columns} values.")
                continue

            try:
                row = []
                for value in row_input:
                    row.append(float(value))
                matrix.append(row)
                break
            except ValueError:
                print("Error: All matrix values must be numbers.")

    return matrix


def display_matrix(matrix):
    for row in matrix:
        for value in row:
            print(f"{value:10g}", end="")
        print()


def transpose_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    result = []

    for column in range(columns):
        new_row = []
        for row in range(rows):
            new_row.append(matrix[row][column])
        result.append(new_row)

    return result


def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    columns = len(matrix_a[0])
    result = []

    for row in range(rows):
        new_row = []
        for column in range(columns):
            value = matrix_a[row][column] + matrix_b[row][column]
            new_row.append(value)
        result.append(new_row)

    return result


def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    columns_a = len(matrix_a[0])
    columns_b = len(matrix_b[0])
    result = []

    for row in range(rows_a):
        new_row = []
        for column in range(columns_b):
            total = 0
            for position in range(columns_a):
                total += matrix_a[row][position] * matrix_b[position][column]
            new_row.append(total)
        result.append(new_row)

    return result


def get_positive_integer(message):
    try:
        value = int(input(message))
    except ValueError:
        return None

    if value <= 0:
        return None
    return value


def main():
    print("============================")
    print("     MATRIX OPERATIONS")
    print("============================")
    print("1. Transpose a matrix")
    print("2. Add two matrices")
    print("3. Multiply two matrices")

    choice = input("Select an operation (1-3): ")

    if choice not in ("1", "2", "3"):
        print("Error: Invalid menu choice.")
        return

    rows = get_positive_integer("Enter number of rows: ")
    columns = get_positive_integer("Enter number of columns: ")

    if rows is None or columns is None:
        print("Error: Matrix dimensions must be positive integers.")
        return

    if choice == "1":
        matrix = read_matrix(rows, columns, "A")
        result = transpose_matrix(matrix)
        print("\nTransposed Matrix:")
        display_matrix(result)

    elif choice == "2":
        matrix_a = read_matrix(rows, columns, "A")
        matrix_b = read_matrix(rows, columns, "B")
        result = add_matrices(matrix_a, matrix_b)
        print("\nSum of the Matrices:")
        display_matrix(result)

    else:
        columns_b = get_positive_integer("Enter number of columns in matrix B: ")
        if columns_b is None:
            print("Error: Matrix dimensions must be positive integers.")
            return

        matrix_a = read_matrix(rows, columns, "A")
        matrix_b = read_matrix(columns, columns_b, "B")
        result = multiply_matrices(matrix_a, matrix_b)
        print("\nProduct of the Matrices:")
        display_matrix(result)


if __name__ == "__main__":
    main()
