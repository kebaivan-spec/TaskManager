tasks = []

while True:

    print("\n1 - Add task")
    print("2 - Show tasks")
    print("3 - Exit")

    choice = input("Choice: ")

    if choice == "1":
        task = input("Task: ")
        tasks.append(task)

    elif choice == "2":
        print(tasks)

    elif choice == "3":
        break