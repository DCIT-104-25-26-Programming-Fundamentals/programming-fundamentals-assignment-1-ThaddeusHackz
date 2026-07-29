

def get_grade(score):
    if score < 0 or score > 100:
        return None
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"


def main():
    try:
        score = float(input("Enter student score (0-100): "))
    except ValueError:
        print("Error: Please enter a valid number.")
        return

    grade = get_grade(score)

    if grade is None:
        print("Error: Score must be between 0 and 100.")
    else:
        print(f"Grade: {grade}")


if __name__ == "__main__":
    main()
