import os
import json

TASKS_FILE = "tasks.json"


def load_tasks():
    """Load tasks from the JSON file, return an empty list if file doesn't exist."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    """Add a task to the list."""
    task = input("Enter the task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f"✅ Task added: {task}")
    else:
        print("⚠️ Task cannot be empty.")


def view_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("📭 No tasks found.")
    else:
        print("\n📝 To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
        print()


def remove_task(tasks):
    """Remove a task by index."""
    view_tasks(tasks)
    if not tasks:
        return

    try:
        index = int(input("Enter the task number to remove: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            save_tasks(tasks)
            print(f"🗑️ Removed task: {removed}")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")


def main():
    """Main application loop."""
    tasks = load_tasks()

    while True:
        print("\n📌 To-Do List Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
