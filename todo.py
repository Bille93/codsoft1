import json
import os
import datetime

# Define the file path for the JSON data
DATA_FILE = 'todos.json'

def load_todos():
    """Load the to-do list from a JSON file"""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_todos(todos):
    """Save the to-do list to a JSON file"""
    with open(DATA_FILE, 'w') as f:
        json.dump(todos, f, indent=4)

def print_todos(todos):
    """Print the to-do list"""
    print("To-Do List:")
    for index, todo in enumerate(todos, start=1):
        print(f"{index}. {todo['task']} (Created: {todo['created']}, Due: {todo['due']})")

def add_todo(todos):
    """Add a new to-do item"""
    task = input("Enter the task: ")
    due = input("Enter the due date (YYYY-MM-DD): ")
    try:
        due_date = datetime.datetime.strptime(due, '%Y-%m-%d').date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return
    todos.append({'task': task, 'created': str(datetime.date.today()), 'due': due})
    save_todos(todos)
    print("Task added successfully.")

def remove_todo(todos):
    """Remove an existing to-do item"""
    print_todos(todos)
    index = int(input("Enter the index of the task to remove: ")) - 1
    if 0 <= index < len(todos):
        del todos[index]
        save_todos(todos)
        print("Task removed successfully.")
    else:
        print("Invalid index.")

def mark_done(todos):
    """Mark a to-do item as done"""
    print_todos(todos)
    index = int(input("Enter the index of the task to mark as done: ")) - 1
    if 0 <= index < len(todos):
        todos[index]['done'] = True
        save_todos(todos)
        print("Task marked as done.")
    else:
        print("Invalid index.")

def show_menu():
    """Display the menu options"""
    print("\nTo-Do List Application")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Done")
    print("5. Exit")

def main():
    """Main function"""
    todos = load_todos()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            print_todos(todos)
        elif choice == '2':
            add_todo(todos)
        elif choice == '3':
            remove_todo(todos)
        elif choice == '4':
            mark_done(todos)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
