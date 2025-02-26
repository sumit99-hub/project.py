import tkinter as tk
from tkinter import messagebox
import sqlite3
def login_screen():
    global login_window
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


def login_verify(email, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    user = c.fetchone()
    conn.close()
    
    if user:
        messagebox.showinfo("Success", "Login Successful")
        login_window.destroy()
        open_dashboard()
    else:
        messagebox.showerror("Error", "Invalid Email or Password")


def open_dashboard():
    dashboard_window = tk.Tk()
    dashboard_window.title("Dashboard - Seat Selection")
    dashboard_window.geometry("600x400")
    dashboard_window.configure(bg="#f0f0f0")


    tk.Label(dashboard_window, text="Select Your Seat", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333").pack(pady=10)


    seat_frame = tk.Frame(dashboard_window, bg="#f0f0f0")
    seat_frame.pack(pady=20)

 
    seats = []
    for row in range(5):
        row_seats = []
        for col in range(5):
            seat = tk.Button(seat_frame, text=f"{row+1}{chr(65+col)}", font=("Arial", 12), bg="white", fg="black", width=4, height=2,
                             command=lambda r=row, c=col: select_seat(r, c, seats))
            seat.grid(row=row, column=col, padx=5, pady=5)
            row_seats.append(seat)
        seats.append(row_seats)

   
    selected_seat_label = tk.Label(dashboard_window, text="Selected Seat: None", font=("Arial", 14), bg="#f0f0f0", fg="#333")
    selected_seat_label.pack(pady=10)

   
    confirm_button = tk.Button(dashboard_window, text="Confirm Selection", font=("Arial", 12), bg="green", fg="white",
                               command=lambda: confirm_selection(selected_seat_label.cget("text")))
    confirm_button.pack(pady=10)


    def select_seat(row, col, seats):
        for r in range(5):
            for c in range(5):
                seats[r][c].config(bg="white")  
        seats[row][col].config(bg="lightgreen") 
        selected_seat_label.config(text=f"Selected Seat: {row+1}{chr(65+col)}")

 
    def confirm_selection(selected_seat):
        if "None" not in selected_seat:
            messagebox.showinfo("Success", f"Seat {selected_seat.split(': ')[1]} confirmed!")
        else:
            messagebox.showerror("Error", "Please select a seat first.")

    dashboard_window.mainloop()

login_screen()