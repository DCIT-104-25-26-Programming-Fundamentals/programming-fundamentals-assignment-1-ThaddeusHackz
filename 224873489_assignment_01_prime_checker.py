

def is_prime(number):
    if number < 2:
        return False

    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1

    return True


def main():
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Error: Please enter a whole number.")
        return

    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is NOT a prime number.")


if __name__ == "__main__":
    main()
