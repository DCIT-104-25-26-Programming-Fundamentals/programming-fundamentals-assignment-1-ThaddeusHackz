
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
