

def add(first_number, second_number):
    return first_number + second_number


def subtract(first_number, second_number):
    return first_number - second_number


def multiply(first_number, second_number):
    return first_number * second_number


def divide(first_number, second_number):
    if second_number == 0:
        return None
    return round(first_number / second_number, 2)


def modulus(first_number, second_number):
    if second_number == 0:
        return None
    return first_number % second_number


def exponentiate(first_number, second_number):
    return first_number ** second_number


def display_menu():
    print("\n============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def main():
    while True:
        display_menu()
        choice = input("Select an operation (1-7): ")

        if choice == "7":
            print("Goodbye!")
            break

        if choice not in ("1", "2", "3", "4", "5", "6"):
            print("Error: Please enter a choice from 1 to 7.")
            continue

        try:
            first_number = float(input("Enter first number : "))
            second_number = float(input("Enter second number: "))
        except ValueError:
            print("Error: Please enter valid numbers.")
            continue

        if choice == "1":
            result = add(first_number, second_number)
            symbol = "+"
        elif choice == "2":
            result = subtract(first_number, second_number)
            symbol = "-"
        elif choice == "3":
            result = multiply(first_number, second_number)
            symbol = "*"
        elif choice == "4":
            result = divide(first_number, second_number)
            symbol = "/"
            if result is None:
                print("Error: Cannot divide by zero.")
                continue
        elif choice == "5":
            result = modulus(first_number, second_number)
            symbol = "%"
            if result is None:
                print("Error: Cannot calculate modulus by zero.")
                continue
        else:
            result = exponentiate(first_number, second_number)
            symbol = "**"

        print(f"Result: {first_number:g} {symbol} {second_number:g} = {result:g}")


if __name__ == "__main__":
    main()
