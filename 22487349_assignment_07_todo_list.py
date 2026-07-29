

def add_task(tasks):
    task = input("Enter task: ").strip()

    if task == "":
        print("Error: A task cannot be empty.")
        return

    tasks.append(task)
    print(f'Task added: "{task}"')


def view_tasks(tasks):
    if len(tasks) == 0:
        print("Your task list is empty.")
        return

    print("Your Tasks:")
    for number in range(len(tasks)):
        print(f"{number + 1}. {tasks[number]}")


def delete_task(tasks):
    if len(tasks) == 0:
        print("Your task list is empty. There is nothing to delete.")
        return

    view_tasks(tasks)

    try:
        task_number = int(input("Enter task number to delete: "))
    except ValueError:
        print("Error: Please enter a valid task number.")
        return

    if task_number < 1 or task_number > len(tasks):
        print("Error: Invalid task number.")
        return

    removed_task = tasks.pop(task_number - 1)
    print(f'Task "{removed_task}" has been removed.')


def display_menu():
    print("\n============================")
    print("     TO-DO LIST MENU")
    print("============================")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")


def main():
    tasks = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Please enter a choice from 1 to 4.")


if __name__ == "__main__":
    main()
