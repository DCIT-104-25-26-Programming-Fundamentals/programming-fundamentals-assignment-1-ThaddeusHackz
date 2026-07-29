
def generate_fibonacci(number_of_terms):
    sequence = []
    first = 0
    second = 1

    for _ in range(number_of_terms):
        sequence.append(first)
        next_number = first + second
        first = second
        second = next_number

    return sequence


def is_fibonacci(number):
    if number < 0:
        return False

    first = 0
    second = 1

    while first < number:
        next_number = first + second
        first = second
        second = next_number

    return first == number


def main():
    try:
        number_of_terms = int(input("How many terms? "))
    except ValueError:
        print("Error: Please enter a positive integer.")
        return

    if number_of_terms <= 0:
        print("Error: The number of terms must be greater than zero.")
        return

    sequence = generate_fibonacci(number_of_terms)
    print("Fibonacci sequence:", end=" ")
    for number in sequence:
        print(number, end=" ")
    print()

    try:
        number_to_check = int(input("Enter a number to check: "))
    except ValueError:
        print("Error: Please enter a whole number.")
        return

    if is_fibonacci(number_to_check):
        print(f"{number_to_check} is a Fibonacci number.")
    else:
        print(f"{number_to_check} is NOT a Fibonacci number.")


if __name__ == "__main__":
    main()
