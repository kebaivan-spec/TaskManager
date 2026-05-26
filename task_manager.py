tasks = []

while True:

    print("Task Manager")
    print("\n1 - Add task")
    print("2 - Show tasks")
    print("3 - Exit")
    print("4 - Clear tasks")

    choice = input("Choice: ")

    if choice == "1":
        task = input("Task: ")
        tasks.append(task)

    elif choice == "2":
        print("FEATURE BRANCH TASKS:", tasks)

    elif choice == "4":
        tasks.clear()
        print("Tasks cleared")

    elif choice == "3":
        break
