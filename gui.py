import tkinter as tk
from tkinter import simpledialog, messagebox

tasks = []

def add_task():
    new_task = simpledialog.askstring("Add Task", "Enter New Task:")
    if new_task:
        tasks.append(new_task)
        messagebox.showinfo("Success", "New Task Added Successfully!")

def update_task():
    if not tasks:
        messagebox.showwarning("No Tasks", "No tasks available to update.")
        return

    old_task = simpledialog.askstring("Update Task", "Enter the task to be updated:")
    if old_task in tasks:
        new_task = simpledialog.askstring("Update Task", "Enter the New Task:")
        index = tasks.index(old_task)
        tasks[index] = new_task
        messagebox.showinfo("Success", "Task Updated Successfully!")
    else:
        messagebox.showerror("Error", "Task not found!")

def delete_task():
    if not tasks:
        messagebox.showwarning("No Tasks", "No tasks available to delete.")
        return

    task_to_delete = simpledialog.askstring("Delete Task", "Enter the task to be deleted:")
    if task_to_delete in tasks:
        tasks.remove(task_to_delete)
        messagebox.showinfo("Success", "Task Deleted Successfully!")
    else:
        messagebox.showerror("Error", "Task not found!")

def view_tasks():
    if not tasks:
        messagebox.showinfo("No Tasks", "No tasks available.")
    else:
        tasks_str = "\n".join(tasks)
        messagebox.showinfo("Your Tasks", tasks_str)

def exit_app():
    root.quit()

# Create the main window
root = tk.Tk()
root.title("TO-DO Tasks Application BY OP")

# Set the background color of the main window
root.configure(bg='black')

# Title label
title_label = tk.Label(root, text="Welcome to TO-DO Application BY OP", font=("Helvetica", 20, "bold"), fg='green', bg='black')
title_label.pack(pady=20)

# Button configurations
button_config = {
    'fg': 'green',
    'bg': 'black',
    'activeforeground': 'green',
    'activebackground': 'black',
    'width': 20
}

# Buttons
add_button = tk.Button(root, text="Add Task", command=add_task, **button_config)
add_button.pack(pady=10)

update_button = tk.Button(root, text="Update Task", command=update_task, **button_config)
update_button.pack(pady=10)

delete_button = tk.Button(root, text="Delete Task", command=delete_task, **button_config)
delete_button.pack(pady=10)

view_button = tk.Button(root, text="View Tasks", command=view_tasks, **button_config)
view_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=exit_app, **button_config)
exit_button.pack(pady=10)

# Run the application
root.mainloop()