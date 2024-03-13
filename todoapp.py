import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sql

def add_task():
    task_string = task_field.get().strip()
    if len(task_string) == 0:
        messagebox.showinfo('Error', 'Task field is empty.')
    else:
        tasks.append(task_string)
        the_cursor.execute('INSERT INTO tasks VALUES (?)', (task_string,))
        list_update()
        task_field.delete(0, 'end')

def list_update():
    clear_list()
    for task in tasks:
        task_listbox.insert('end', task)

def delete_task():
    try:
        selected_task = task_listbox.curselection()
        if selected_task:
            index = selected_task[0]
            task_value = task_listbox.get(index)
            tasks.remove(task_value)
            the_cursor.execute('DELETE FROM tasks WHERE title = ?', (task_value,))
            list_update()
    except:
        messagebox.showinfo('Error', 'No task selected. Unable to delete.')

def delete_all_tasks():
    confirmed = messagebox.askyesno('Delete All', 'Are you sure you want to delete all tasks?')
    if confirmed:
        tasks.clear()
        the_cursor.execute('DELETE FROM tasks')
        list_update()

def clear_list():
    task_listbox.delete(0, 'end')

def close():
    print('Tasks:', tasks)
    guiWindow.destroy()

def retrieve_database():
    tasks.clear()
    for row in the_cursor.execute('SELECT title FROM tasks'):
        tasks.append(row[0])

if __name__ == "__main__":
    guiWindow = tk.Tk()
    guiWindow.title("To-Do List Manager")
    guiWindow.geometry("400x400+500+200")
    guiWindow.resizable(0, 0)
    guiWindow.configure(bg="#F0F0F0")

    the_connection = sql.connect('tasklist.db')
    the_cursor = the_connection.cursor()
    the_cursor.execute('CREATE TABLE IF NOT EXISTS tasks (title TEXT)')

    tasks = []

    header_frame = tk.Frame(guiWindow, bg="#6495ED")
    header_frame.pack(fill="x")

    header_label = ttk.Label(
        header_frame,
        text="To-Do List Manager",
        font=("Arial", 18),
        background="#6495ED",
        foreground="#FFFFFF"
    )
    header_label.pack(pady=10)

    input_frame = tk.Frame(guiWindow, bg="#F0F0F0")
    input_frame.pack(fill="x")

    task_label = ttk.Label(
        input_frame,
        text="Enter Task:",
        font=("Arial", 12),
        background="#F0F0F0",
        foreground="#000000"
    )
    task_label.pack(side="left", padx=10, pady=10)

    task_field = ttk.Entry(
        input_frame,
        font=("Arial", 12),
        width=25,
        background="#FFFFFF",
        foreground="#000000"
    )
    task_field.pack(side="left", padx=10, pady=10)

    button_frame = tk.Frame(guiWindow, bg="#F0F0F0")
    button_frame.pack(fill="x")

    add_button = ttk.Button(
        button_frame,
        text="Add Task",
        width=15,
        command=add_task
    )
    add_button.pack(side="left", padx=10, pady=10)

    delete_button = ttk.Button(
        button_frame,
        text="Delete Task",
        width=15,
        command=delete_task
    )
    delete_button.pack(side="left", padx=10, pady=10)

    delete_all_button = ttk.Button(
        button_frame,
        text="Delete All Tasks",
        width=15,
        command=delete_all_tasks
    )
    delete_all_button.pack(side="left", padx=10, pady=10)

    task_listbox = tk.Listbox(
        guiWindow,
        width=40,
        height=15,
        background="#FFFFFF",
        foreground="#000000",
        selectbackground="#87CEEB",
        selectforeground="#FFFFFF"
    )
    task_listbox.pack(padx=10, pady=20)

    retrieve_database()
    list_update()
    guiWindow.mainloop()

    the_connection.commit()
    the_cursor.close()
