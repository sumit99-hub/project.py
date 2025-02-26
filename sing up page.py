
import tkinter as tk
from tkinter import messagebox
import sqlite3
def initialize_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  email TEXT NOT NULL UNIQUE,
                  contact TEXT NOT NULL,
                  password TEXT NOT NULL)''')
    conn.commit()
    conn.close()
def sign_up():
    name = name_entry.get()
    email = email_entry.get()
    contact = contact_entry.get()
    password = password_entry.get()

    if name and email and contact and password:
        try:
            conn = sqlite3.connect('users.db')
            c = conn.cursor()
            c.execute("INSERT INTO users (name, email, contact, password) VALUES (?, ?, ?, ?)",
                      (name, email, contact, password))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Signed up successfully!")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Email already exists!")
    else:
        messagebox.showerror("Error", "Please fill in all fields")
root = tk.Tk()
root.title("Sign Up")
root.geometry("600x350")
root.configure(bg="#eaf7f5")
left_frame = tk.Frame(root, bg="#2d5d77", width=250, height=350)
left_frame.pack(side="left", fill="y")
right_frame = tk.Frame(root, bg="#eaf7f5", width=350, height=350)
right_frame.pack(side="right", fill="both", expand=True)


left_frame.grid_propagate(False)
left_frame.columnconfigure(0, weight=1)
left_frame.rowconfigure(0, weight=1)
left_inner_frame = tk.Frame(left_frame, bg="#2d5d77")
left_inner_frame.grid(sticky="nsew")

welcome_label = tk.Label(left_inner_frame, text="Welcome Back", font=("Arial", 14, "bold"), bg="#2d5d77", fg="white")
welcome_label.pack(pady=20)
create_account_button = tk.Button(left_inner_frame, text="Create Account", bg="blue", fg="black", borderwidth=2, relief="ridge")
create_account_button.pack()


right_frame.grid_propagate(False)
right_frame.columnconfigure(0, weight=1)
right_frame.rowconfigure(0, weight=1)
right_inner_frame = tk.Frame(right_frame, bg="#eaf7f5")
right_inner_frame.grid(sticky="nsew")

title_label = tk.Label(right_inner_frame, text="Sign Up!", font=("Arial", 16, "bold"), bg="#eaf7f5", fg="#2d5d77")
title_label.pack(pady=10)


fields = [
    ("Name:", tk.Entry(right_inner_frame, width=30)),
    ("Email:", tk.Entry(right_inner_frame, width=30)),
    ("Contact No:", tk.Entry(right_inner_frame, width=30)),
    ("Password:", tk.Entry(right_inner_frame, width=30, show="*"))
]

for label_text, entry_widget in fields:
    label = tk.Label(right_inner_frame, text=label_text, bg="#eaf7f5", fg="#333")
    label.pack(pady=2)
    entry_widget.pack(pady=2)

name_entry, email_entry, contact_entry, password_entry = [field[1] for field in fields]

sign_up_button = tk.Button(right_inner_frame, text="Sign Up", command=sign_up, bg="white", fg="black", width=15, borderwidth=2, relief="ridge")
sign_up_button.pack(pady=15)


initialize_db()
root.mainloop()