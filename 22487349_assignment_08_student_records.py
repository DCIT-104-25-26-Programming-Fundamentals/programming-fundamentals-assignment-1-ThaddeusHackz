
def calculate_average(scores):
    if len(scores) == 0:
        return 0

    total = 0
    for score in scores:
        total += score

    return round(total / len(scores), 2)


def find_student(students, student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None


def add_student(students):
    name = input("Student name: ").strip()
    if name == "":
        print("Error: Student name cannot be empty.")
        return

    try:
        student_id = int(input("Student ID: "))
    except ValueError:
        print("Error: Student ID must be a number.")
        return

    if find_student(students, student_id) is not None:
        print("Error: A student with this ID already exists.")
        return

    try:
        number_of_scores = int(input("How many scores? "))
    except ValueError:
        print("Error: Please enter a positive number of scores.")
        return

    if number_of_scores <= 0:
        print("Error: The number of scores must be greater than zero.")
        return

    scores = []
    for position in range(1, number_of_scores + 1):
        try:
            score = float(input(f"Enter score {position}: "))
        except ValueError:
            print("Error: Scores must be numbers.")
            return
        scores.append(score)

    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }
    students.append(student)
    print(f'Student "{name}" added successfully.')


def display_all_students(students):
    if len(students) == 0:
        print("No student records have been added yet.")
        return

    print("-" * 75)
    print(f"{'Name':<20}{'ID':<15}{'Scores':<25}{'Average':>10}")
    print("-" * 75)

    for student in students:
        score_text = ""
        for position in range(len(student["scores"])):
            if position > 0:
                score_text += ", "
            score_text += f'{student["scores"][position]:g}'

        average = calculate_average(student["scores"])
        print(f'{student["name"]:<20}{student["id"]:<15}{score_text:<25}{average:>10.2f}')

    print("-" * 75)


def display_student_average(students):
    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print("Error: Student ID must be a number.")
        return

    student = find_student(students, student_id)
    if student is None:
        print("Error: Student ID not found.")
        return

    average = calculate_average(student["scores"])
    print(f'{student["name"]}\'s average score: {average:.2f}')


def display_menu():
    print("\n================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


def main():
    students = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_all_students(students)
        elif choice == "3":
            display_student_average(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Please enter a choice from 1 to 4.")


if __name__ == "__main__":
    main()
