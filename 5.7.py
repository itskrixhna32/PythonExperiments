#7.	Create a Todo list Manager where users can add, view, and remove tasks. Use List for storing tasks.
todo_list = []
def add_task(task):
    todo_list.append(task)
def view_tasks():
    if not todo_list:
        print("No tasks in the Todo list.")
    else:
        print("Todo List:")
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")
def remove_task(task_number):
    if 1 <= task_number <= len(todo_list):
        todo_list.pop(task_number - 1)
        print("Task removed successfully.")
    else:
        print("Invalid task number.")
while True:
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        task = input("Enter the task to add: ")
        add_task(task)
        print("Task added successfully.")
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        view_tasks()
        task_number = int(input("Enter the task number to remove: "))
        remove_task(task_number)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
        