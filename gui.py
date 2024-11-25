import tkinter as tk
from tkinter import messagebox
from task_manager import *
from file_handler import *

window = tk.Tk()
window.title("To-Do List App")

tasks = []
filename = "tasks.txt"


def gui_display_tasks():
    tasks = load_tasks_from_file(filename)
    listbox_tasks.delete(0, tk.END) # Clear the Listbox
    for index, task in enumerate(tasks, 1):
        listbox_tasks.insert(tk.END, f"{task['name']} - {task['priority']} - {task['due_date']} - {task['category']}")


label_entry = tk.Label(window, text= "Task name")
label_priority = tk.Label(window, text= "Priority")
label_due_date = tk.Label(window, text= "Due date")
label_category = tk.Label(window, text= "Task name")

entry_task = tk.Entry(window, width=50)
entry_priority = tk.Entry(window, width=50)
entry_due_date = tk.Entry(window, width=50)
entry_category = tk.Entry(window, width=50)

label_entry.grid(row=0, column=0, padx=5, pady=5, sticky="e")
label_priority.grid(row=1, column=0, padx=5, pady=5, sticky="e")
label_due_date.grid(row=2, column=0, padx=5, pady=5, sticky="e")
label_category.grid(row=3, column=0, padx=5, pady=5, sticky="e")

entry_task.grid(row=0, column=1, padx=5, pady=5)
entry_priority.grid(row=1, column=1, padx=5, pady=5)
entry_due_date.grid(row=2, column=1, padx=5, pady=5)
entry_category.grid(row=3, column=1, padx=5, pady=5)

# Create a listbox for displaying tasks
listbox_tasks = tk.Listbox(window, height=10, width=50)
listbox_tasks.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

# create a scrollbar for the listbox
scrollbar_tasks = tk.Scrollbar(window)
scrollbar_tasks.grid(row=4, column=3, sticky="ns")

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)



# Load and display tasks at startup
gui_display_tasks()

# Define add_task function for the GUI
def gui_add_task():
    tasks = load_tasks_from_file(filename)  # Load existing tasks
    task_name = entry_task.get()
    priority = entry_priority.get().lower()
    due_date = entry_due_date.get()
    category = entry_category.get().lower()

    if task_name and priority and due_date and category:
        add_task(tasks, task_name, priority, due_date, category)
        listbox_tasks.insert(tk.END, f"{task_name} - {priority} - {due_date} - {category}")
        # clear the entry after adding the task
        entry_task.delete(0, tk.END)
        entry_priority.delete(0, tk.END)
        entry_due_date.delete(0, tk.END)
        entry_category.delete(0, tk.END)
        save_tasks_to_file(filename, tasks)
    else:
        messagebox.showwarning("Warning", "All fields must be filled out.")

# Create a button to add tasks
button_add_task = tk.Button(window, text="Add Task", command=gui_add_task)
button_add_task.grid(row=5, column=0, pady=5)


# Define delete_task function for the GUI
def gui_delete_task():
    tasks = load_tasks_from_file(filename)  # Load existing tasks
    try:
        # Gets the first selected index
        selected_task_index = listbox_tasks.curselection()[0]
        # Removes the corresponding item from the tasks list
        delete_task(tasks, selected_task_index)
        # Removes the selected item from the listbox
        listbox_tasks.delete(selected_task_index)
        save_tasks_to_file(filename, tasks)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task.")

# Create a button to delete tasks
button_delete_task = tk.Button(window, text="Delete Task", command=gui_delete_task)
button_delete_task.grid(row=5, column=1, pady=5)


def gui_sort_priority():
    tasks = load_tasks_from_file(filename)  # Load existing tasks
    sort_tasks_by_priority(tasks)
    listbox_tasks.delete(0, tk.END)
    for task in tasks:
        # insert from tk.END where is 0 (because all tasks were deleted)
        listbox_tasks.insert(tk.END, f"{task['name']} - {task['priority']} - {task['due_date']} - {task['category']}")
    save_tasks_to_file(filename, tasks)

button_sort_priority = tk.Button(window, text="Sort by Priority", command=gui_sort_priority)
button_sort_priority.grid(row=5, column=2, pady=5)

# Run the application
window.mainloop()