import os

FILE_NAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                task, status = line.strip().split("|")
                tasks.append({"task": task, "done": status == "True"})
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for t in tasks:
            file.write(f"{t['task']}|{t['done']}\n")

# Show all tasks
def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
        return
    print("\nYour Tasks:")
    for i, t in enumerate(tasks, 1):
        status = "✔" if t["done"] else "✘"
        print(f"{i}. [{status}] {t['task']}")
    print()

# Add new task
def add_task(tasks):
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print("Task added!\n")

# Delete task
def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        removed = tasks.pop(num - 1)
        save_tasks(tasks)
        print(f"Deleted: {removed['task']}\n")
    except:
        print("Invalid input!\n")

# Mark task as completed
def mark_done(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to mark complete: "))
        tasks[num - 1]["done"] = True
        save_tasks(tasks)
        print("Task marked as completed!\n")
    except:
        print("Invalid input!\n")

# Update task
def update_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to update: "))
        new_task = input("Enter new task: ")
        tasks[num - 1]["task"] = new_task
        save_tasks(tasks)
        print("Task updated!\n")
    except:
        print("Invalid input!\n")

# Main menu
def main():
    tasks = load_tasks()

    while True:
        print("==== TO-DO LIST MENU ====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Done")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            mark_done(tasks)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!\n")

if __name__ == "__main__":
    main()
