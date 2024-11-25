from task_manager import *
from file_handler import *
from menu import *


filename = 'tasks.txt'
tasks = load_tasks_from_file(filename)
sort_tasks_by_priority(tasks)


while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        add_task(tasks)
        sort_tasks_by_priority(tasks)
        save_tasks_to_file(filename, tasks)
    elif choice == '2':
        display_tasks(tasks)
        input("Press Enter to go back to the menu...")
    elif choice == '3':
        sort_tasks_by_due_date(tasks)
        display_tasks(tasks)
        input("Press Enter to go back to the menu...")
    elif choice == '4':
        filter_tasks_by_category(tasks)
        input("Press Enter to go back to the menu...")
    elif choice == '5':
        filter_tasks_by_status(tasks)
        input("Press Enter to go back to the menu...")
    elif choice == '6':
        mark_task_as_completed(tasks)
    elif choice == '7':
        search_tasks_by_keyword(tasks)
        input("Press Enter to go back to the menu...")
    elif choice == '8':
        display_tasks(tasks)
        delete_task(tasks)
        save_tasks_to_file(filename, tasks)
    elif choice == '9':
        break
    else:
        print("Invalid choice, please try again.")
