# Console-Based To-Do List App

# Step 1: Create an empty list to store tasks
todo_list = []

# Step 2: Function to show the menu
def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

# Step 3: Function to display all tasks
def view_tasks():
    if not todo_list:
        print("✅ Your to-do list is empty!")
    else:
        print("\n📋 Your Tasks:")
        for index, task in enumerate(todo_list, start=1):
            status = "✔️" if task["completed"] else "❌"
            print(f"{index}. {task['title']} [{status}]")

# Step 4: Function to add a task
def add_task():
    title = input("Enter the task title: ")
    task = {"title": title, "completed": False}
    todo_list.append(task)
    print(f"🆕 Task '{title}' added successfully!")

# Step 5: Function to mark a task as completed
def mark_completed():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_num <= len(todo_list):
            todo_list[task_num - 1]["completed"] = True
            print("✅ Task marked as completed!")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

# Step 6: Function to delete a task
def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(todo_list):
            removed = todo_list.pop(task_num - 1)
            print(f"🗑️ Task '{removed['title']}' deleted.")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

# Step 7: Main loop to run the menu
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_completed()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("👋 Exiting... Thank you for using the To-Do App!")
        break
    else:
        print("⚠️ Invalid choice. Please enter a number from 1 to 5.")
