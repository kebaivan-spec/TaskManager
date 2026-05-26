class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def show_tasks(self):
        if not self.tasks:
            print("Немає задач")
        else:
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")


manager = TaskManager()

while True:

    print("\n1 - Додати задачу")
    print("2 - Видалити задачу")
    print("3 - Показати задачі")
    print("4 - Вихід")

    choice = input("Вибір: ")

    if choice == "1":
        task = input("Введіть задачу: ")
        manager.add_task(task)

    elif choice == "2":
        task = input("Яку задачу видалити?: ")
        manager.remove_task(task)

    elif choice == "3":
        manager.show_tasks()

    elif choice == "4":
        break
