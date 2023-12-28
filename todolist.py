def show_menu():
    print("Todo List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")

def add_task(todo_list, task):
    todo_list.append({"task": task, "completed": False})
    print("Task added successfully!")

def view_tasks(todo_list):
    if not todo_list:
        print("No tasks in the list.")
    else:
        print("Todo List:")
        for i, task in enumerate(todo_list, 1):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{i}. {task['task']} - {status}")

def mark_completed(todo_list, task_index):
    if 1 <= task_index <= len(todo_list):
        todo_list[task_index - 1]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task index.")

def main():
    todo_list = []

    while True:
        show_menu()

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(todo_list, task)
        elif choice == "2":
            view_tasks(todo_list)
        elif choice == "3":
            task_index = int(input("Enter the task index to mark as completed: "))
            mark_completed(todo_list, task_index)
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()