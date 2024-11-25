tasks = []

def save_tasks_to_file(filename, tasks):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(f"{task['name']}|{task['priority']}|{task['due_date']}|{task['category']}\n")


def load_tasks_from_file(filename):
    # global tasks  # Ensure we use the global tasks list
    tasks.clear() # Clear the list before loading new tasks
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, priority, due_date, task_category = line.strip().split('|')
                tasks.append({'name': name, 'priority': priority, 'due_date': due_date, 'category': task_category})
    except FileNotFoundError:
        pass
    return tasks
