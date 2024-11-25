import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_menu():
    clear_screen()
    print("=" * 30)
    print(" TO-DO LIST APP ".center(30))
    print("=" * 30)
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. View all tasks (Sort by due time)")
    print("4. Filter tasks by category")
    print("5. Filter tasks by status")
    print("6. Mark a task as completed")
    print("7. Search tasks by keyword")
    print("8. Delete a task")
    print("9. Exit")
    print("=" * 30)
