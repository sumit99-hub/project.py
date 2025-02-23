import tkinter as tk
from tkinter import messagebox



# Login Screen
def login_screen():
    login_window = tk.Tk()
    login_window.title("Welcome Back - Login")
    login_window.geometry("400x400")
    login_window.configure(bg="lightblue")
    
    tk.Label(login_window, text="Welcome Back", font=("Arial", 16, "bold"), bg="lightblue", fg="blue").pack(pady=10)
    tk.Label(login_window, text="Email", font=("Arial", 12), bg="lightblue", fg="black").pack()
    email_entry = tk.Entry(login_window, font=("Arial", 12), fg="black", bg="white")
    email_entry.pack()
    
    tk.Label(login_window, text="Password", font=("Arial", 12), bg="lightblue", fg="black").pack()
    password_entry = tk.Entry(login_window, font=("Arial", 12), fg="black", bg="white", show="*")
    password_entry.pack()
    
    tk.Button(login_window, text="Login", font=("Arial", 12), bg="blue", fg="black", command=lambda: login_verify(email_entry.get(), password_entry.get())).pack(pady=10)
    
    login_window.mainloop()

# Dummy Login Verification
def login_verify(email, password):
    if email == "user@example.com" and password == "password123":
        messagebox.showinfo("Success", "Login Successful")
    else:
        messagebox.showerror("Error", "Invalid Email or Password")

# Run the login screen
login_screen()
