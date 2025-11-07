import tkinter as tk
from tkinter import ttk, messagebox

# --- Data Lists ---
todo_list = []
deleted_tasks = []
completed_tasks = []

# --- Functions ---
def add_task():
    title, desc = title_entry.get(), desc_entry.get()
    if not title or not desc:
        messagebox.showerror("Error", "All fields are required!")
        return
    task = {"title": title, "desc": desc, "status": "Pending"}
    todo_list.append(task)
    update_tables()
    clear_fields()
    messagebox.showinfo("Success", "Task added successfully!")

def delete_task():
    selected = pending_table.selection()
    if not selected:
        messagebox.showerror("Error", "Select a task to delete")
        return
    index = pending_table.index(selected[0])
    deleted_tasks.append(todo_list[index].copy())
    todo_list.pop(index)
    update_tables()
    messagebox.showinfo("Deleted", "Task deleted successfully!")

def mark_completed():
    selected = pending_table.selection()
    if not selected:
        messagebox.showerror("Error", "Select a task to mark as completed")
        return
    index = pending_table.index(selected[0])
    task = todo_list.pop(index)
    task["status"] = "Completed"
    completed_tasks.append(task)
    update_tables()
    messagebox.showinfo("Done", "Task marked as completed!")

def update_tables():
    def refresh(table, data):
        table.delete(*table.get_children())
        for task in data:
            table.insert("", "end", values=(task["title"], task["desc"], task["status"]))
    refresh(pending_table, todo_list)
    refresh(deleted_table, deleted_tasks)
    refresh(completed_table, completed_tasks)

def clear_fields():
    for entry in (title_entry, desc_entry):
        entry.delete(0, tk.END)

# --- GUI Setup ---
root = tk.Tk()
root.title("📝 To-Do List Management System")
root.geometry("850x650")
root.config(bg="#f7f9fb")

tk.Label(root, text="To-Do List Management System", font=("Arial", 20, "bold"),
         fg="#2c3e50", bg="#f7f9fb").pack(pady=15)

# Input Frame
frame = tk.Frame(root, bg="#f7f9fb")
frame.pack(pady=10)

labels = ["Task Title:", "Description:"]
entries = []
for i, text in enumerate(labels):
    tk.Label(frame, text=text, font=("Arial", 11, "bold"), bg="#f7f9fb", fg="#2c3e50").grid(row=i, column=0, sticky="w", pady=5)
    e = tk.Entry(frame, width=30, font=("Arial", 11))
    e.grid(row=i, column=1, padx=10, pady=5)
    entries.append(e)

title_entry, desc_entry = entries

# Buttons
btn_frame = tk.Frame(root, bg="#f7f9fb")
btn_frame.pack(pady=10)

def make_btn(text, color, cmd, col):
    tk.Button(btn_frame, text=text, bg=color, fg="white", width=14, height=1,
              font=("Arial", 11, "bold"), relief="flat", cursor="hand2",
              command=cmd).grid(row=0, column=col, padx=8)

make_btn("Add Task", "#27ae60", add_task, 0)
make_btn("Delete Task", "#e74c3c", delete_task, 1)
make_btn("Mark Completed", "#2980b9", mark_completed, 2)
make_btn("Clear Fields", "#8e44ad", clear_fields, 3)

# Table Setup
def make_table(title, color):
    tk.Label(root, text=title, bg="#f7f9fb", font=("Arial", 14, "bold"), fg=color).pack()
    t = ttk.Treeview(root, columns=("Title", "Description", "Status"), show="headings", height=6)
    for col in ("Title", "Description", "Status"):
        t.heading(col, text=col)
        t.column(col, width=200)
    t.pack(pady=8)
    return t

pending_table = make_table("Pending Tasks", "#2c3e50")
completed_table = make_table("Completed Tasks", "#27ae60")
deleted_table = make_table("Deleted Tasks", "#c0392b")

root.mainloop()
