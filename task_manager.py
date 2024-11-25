from datetime import datetime
from file_handler import save_tasks_to_file


def add_task(tasks, task_name, priority, due_date, task_category):
    #task_name = input("Enter the task: ")
    #priority = input("Enter the priority (high/medium/low): ").lower()
    #due_date = input("Enter the due day (YYYY-MM-DD): ")

    #while True:
    #    task_category = input("Enter the Category (Work/Personal/Shopping): ").lower()
    #    if task_category in ['work', 'personal', 'shopping']:
    #        break
    #    else:
    #        print("Invalid input! Please enter a valid category (Work/Personal/Shopping).")

    tasks.append({'name': task_name, 'priority': priority, 'due_date': due_date, 'category': task_category})
    print("Task added!")


def display_tasks(tasks):
    today = datetime.today().date()
    for index, task in enumerate(tasks, 1):
        due_date_formatted = datetime.strptime(task['due_date'], '%Y-%m-%d').date()

        if "(Completed)" in task['name']:
            status = "(Completed)"
            task_display_name = task['name'].replace("(Completed)", "").strip()
        else:
            status = ""
            task_display_name = task['name']

        overdue_status = ""
        if today > due_date_formatted:
            overdue_status = " - Overdue!"

        print(f"{index}, {task_display_name} - Priority: {task['priority']} {status} - Due_Date: {task['due_date']}{overdue_status} - Category: {task['category']}")

    print("=" * 30)


def delete_task(tasks, task_number):
    # task_number = int(input("Enter the task number to delete: "))
    if 0 < task_number <= len(tasks):
        tasks.pop(task_number - 1)
        print("Task deleted")


def mark_task_as_completed(tasks):
    display_tasks(tasks)
    task_number = int(input("Enter the task number to mark as completed: "))
    if 0 < task_number <= len(tasks):
        if "(Completed)" not in tasks[task_number - 1]['name']:
            tasks[task_number - 1]['name'] += "(Completed)"
            print("Task marked as completed!")
        else:
            print("Task is already marked as completed.")


def sort_tasks_by_priority(tasks):
    priority_order = {'high': 1, 'medium': 2, 'low': 3}
    tasks.sort(key=lambda task: priority_order[task['priority']])


def sort_tasks_by_due_date(tasks):
    tasks.sort(key=lambda task: datetime.strptime(task['due_date'], '%Y-%m-%d'))


def filter_tasks_by_category(tasks):
    # Code to filter tasks by category
    while True:
        category = input("Enter the Category (Work/Personal/Shopping): ").lower()
        if category in ['work', 'personal', 'shopping']:
            break
        else:
            print("Invalid input! Please enter a valid category (Work/Personal/Shopping).")

    filtered_tasks = [task for task in tasks if task['category'] == category]
    display_tasks(filtered_tasks)


def filter_tasks_by_status(tasks):
    while True:
        status = input("Enter the status (complete/incomplete): ").lower()
        if status in ['complete', 'incomplete']:
            break
        else:
            print("Invalid input! Please enter a valid status (complete/incomplete).")
    if status == 'complete':
        filtered_tasks = [task for task in tasks if "(Completed)" in task['name']]
    else:
        filtered_tasks = [task for task in tasks if "(Completed)" not in task['name']]

    display_tasks(filtered_tasks)


def search_tasks_by_keyword(tasks):
    keyword = input("Enter keyword: ").lower()
    matching_tasks = [task for task in tasks if keyword in task['name'].lower()]
    display_tasks(matching_tasks)