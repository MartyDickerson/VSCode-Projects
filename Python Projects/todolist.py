import json
import os

FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("✅ No tasks yet!")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✔" if task["done"] else "❌"
            print(f"{i}. {task['task']} [{status}]")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- TO-DO LIST ---")
        show_tasks(tasks)
        print("\nOptions: [a]dd, [d]one, [r]emove, [q]uit")
        choice = input("Enter choice: ").lower()

        if choice == "a":
            new_task = input("New task: ")
            tasks.append({"task": new_task, "done": False})
        elif choice == "d":
            num = int(input("Task number done: ")) - 1
            if 0 <= num < len(tasks):
                tasks[num]["done"] = True
        elif choice == "r":
            num = int(input("Task number to remove: ")) - 1
            if 0 <= num < len(tasks):
                tasks.pop(num)
        elif choice == "q":
            save_tasks(tasks)
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
