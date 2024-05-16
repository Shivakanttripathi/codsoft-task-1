import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except IndexError:
        pass

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create the task entry
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Create the Add Task button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

# Create the To-Do List
listbox = tk.Listbox(root, width=50)
listbox.pack()

# Create the Delete Task button
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

# Run the main loop
root.mainloop()