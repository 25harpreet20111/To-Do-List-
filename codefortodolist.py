import tkinter as tk
from tkinter import messagebox
import os

# ------------------ FUNCTIONS ------------------

def add_task():
    task = task_entry.get().strip()
    if task != "":
        task_listbox.insert(tk.END, f"• {task}")
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Input Error", "Please enter a task before adding!")

def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
        save_tasks()
    except:
        messagebox.showwarning("Selection Error", "Please select a task to delete!")

def clear_all_tasks():
    confirm = messagebox.askyesno("Clear All", "Are you sure you want to delete all tasks?")
    if confirm:
        task_listbox.delete(0, tk.END)
        save_tasks()

def save_tasks():
    with open("tasks.txt", "w") as f:
        tasks = task_listbox.get(0, tk.END)
        for t in tasks:
            f.write(t + "\n")

def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as f:
            for line in f:
                task_listbox.insert(tk.END, line.strip())

def mark_done():
    try:
        index = task_listbox.curselection()[0]
        task = task_listbox.get(index)
        if not task.startswith("✅"):
            task_listbox.delete(index)
            task_listbox.insert(index, "✅ " + task)
            save_tasks()
    except:
        messagebox.showinfo("Mark Task", "Select a task to mark as done!")

# ------------------ UI DESIGN ------------------

root = tk.Tk()
root.title("📝 To-Do List App")
root.geometry("500x500")
root.config(bg="#EAF2F8")

# Title
title_label = tk.Label(root, text="🗒️ TO-DO LIST", font=("Comic Sans MS", 22, "bold"),
                       bg="#EAF2F8", fg="#1A5276")
title_label.pack(pady=20)

# Entry Frame
entry_frame = tk.Frame(root, bg="#EAF2F8")
entry_frame.pack(pady=10)

task_entry = tk.Entry(entry_frame, font=("Arial", 14), width=25, bd=2, relief="solid")
task_entry.grid(row=0, column=0, padx=10)

add_button = tk.Button(entry_frame, text="➕ Add Task", font=("Arial", 12, "bold"),
                       bg="#2ECC71", fg="white", width=12, command=add_task)
add_button.grid(row=0, column=1)

# Listbox
task_listbox = tk.Listbox(root, font=("Arial", 14), width=45, height=12,
                          selectbackground="#AED6F1", bg="#FDFEFE", fg="#1B4F72",
                          bd=3, relief="groove")
task_listbox.pack(pady=20)

# Buttons Frame
button_frame = tk.Frame(root, bg="#EAF2F8")
button_frame.pack(pady=10)

delete_button = tk.Button(button_frame, text="🗑️ Delete Task", font=("Arial", 12, "bold"),
                          bg="#E74C3C", fg="white", width=15, command=delete_task)
delete_button.grid(row=0, column=0, padx=10)

done_button = tk.Button(button_frame, text="✅ Mark Done", font=("Arial", 12, "bold"),
                        bg="#5DADE2", fg="white", width=15, command=mark_done)
done_button.grid(row=0, column=1, padx=10)

clear_button = tk.Button(button_frame, text="🧹 Clear All", font=("Arial", 12, "bold"),
                         bg="#F39C12", fg="white", width=15, command=clear_all_tasks)
clear_button.grid(row=1, column=0, columnspan=2, pady=10)

# Footer
footer_label = tk.Label(root, text="Made with Python 🐍 | by Harpreet 💡",
                        font=("Comic Sans MS", 10), bg="#EAF2F8", fg="#5D6D7E")
footer_label.pack(side="bottom", pady=10)

# Load previous tasks
load_tasks()

root.mainloop()

