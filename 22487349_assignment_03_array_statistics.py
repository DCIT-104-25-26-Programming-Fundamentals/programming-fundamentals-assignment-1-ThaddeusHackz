

def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def calculate_average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)


def find_maximum(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum


def find_minimum(numbers):
    minimum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
    return minimum


def main():
    try:
        amount = int(input("How many numbers? "))
    except ValueError:
        print("Error: Please enter a positive integer.")
        return

    if amount <= 0:
        print("Error: The number of values must be greater than zero.")
        return

    numbers = []
    for position in range(1, amount + 1):
        try:
            number = float(input(f"Enter number {position}: "))
        except ValueError:
            print("Error: Please enter valid numbers only.")
            return
        numbers.append(number)

    print("\nResults:")
    print(f"Sum:     {calculate_sum(numbers):g}")
    print(f"Average: {calculate_average(numbers):g}")
    print(f"Maximum: {find_maximum(numbers):g}")
    print(f"Minimum: {find_minimum(numbers):g}")


if __name__ == "__main__":
    main()
