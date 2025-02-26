import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3


def initialize_db():
    conn = sqlite3.connect('bus_tickets.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  email TEXT NOT NULL UNIQUE,
                  contact TEXT NOT NULL,
                  password TEXT NOT NULL)''')
    c.execute('''CREATE TABLE IF NOT EXISTS tickets
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  user_id INTEGER,
                  passenger_name TEXT NOT NULL,
                  seat_number TEXT NOT NULL,
                  bus_no TEXT NOT NULL,
                  bus_route TEXT NOT NULL,
                  date TEXT NOT NULL,
                  time TEXT NOT NULL,
                  payment_method TEXT NOT NULL,
                  FOREIGN KEY(user_id) REFERENCES users(id))''')
    conn.commit()
    conn.close()

def sign_up():
    global name_entry, email_entry, contact_entry, password_entry
    name = name_entry.get()
    email = email_entry.get()
    contact = contact_entry.get()
    password = password_entry.get()

    if name and email and contact and password:
        try:
            conn = sqlite3.connect('bus_tickets.db')
            c = conn.cursor()
            c.execute("INSERT INTO users (name, email, contact, password) VALUES (?, ?, ?, ?)",
                      (name, email, contact, password))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Signed up successfully!")
            root.destroy()
            login_screen()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Email already exists!")
    else:
        messagebox.showerror("Error", "Please fill in all fields")

def login_screen():
    global login_window
    login_window = tk.Tk()
    login_window.title("Welcome Back - Login")
    login_window.geometry("1900x1700")
    login_window.configure(bg="lightblue")
    
    tk.Label(login_window, text="Welcome Back", font=("Arial", 60, "bold"), bg="lightblue", fg="black").pack(pady=40)
    tk.Label(login_window, text="Email", font=("Arial", 30), bg="lightblue", fg="black").pack()
    email_entry = tk.Entry(login_window, font=("Arial", 30), fg="black", bg="lightblue")
    email_entry.pack()
    
    tk.Label(login_window, text="Password", font=("Arial", 30), bg="lightblue", fg="black").pack()
    password_entry = tk.Entry(login_window, font=("Arial",30), fg="black", bg="lightblue", show="*")
    password_entry.pack()
    
    tk.Button(login_window, text="Login", font=("Arial", 30), bg="lightblue", fg="black", command=lambda: login_verify(email_entry.get(), password_entry.get())).pack(pady=40)
    tk.Button(login_window, text="Forget Password", font=("Arial", 40), bg="lightblue", fg="black", command=forget_password_screen).pack(pady=40)
    
    login_window.mainloop()
def forget_password_screen():
    root = tk.Tk()
    ForgetPasswordApp(root)
    root.mainloop()
    root.mainloop()

def login_verify(email, password):
    conn = sqlite3.connect('bus_tickets.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    user = c.fetchone()
    conn.close()
    
    if user:
        messagebox.showinfo("Success", "Login Successful")
        login_window.destroy()
        open_dashboard(user[0])
    else:
        messagebox.showerror("Error", "Invalid Email or Password")

def open_dashboard(user_id):
    dashboard_window = tk.Tk()
    dashboard_window.title("Dashboard")
    dashboard_window.geometry("1900x1700")
    dashboard_window.configure(bg="lightblue")

    tk.Label(dashboard_window, text="Dashboard", font=("Arial", 60, "bold"), bg="lightblue", fg="black").pack(pady=40)

    tk.Button(dashboard_window, text="Book Ticket", font=("Arial", 35), bg="white", fg="black", command=lambda: open_seat_selection(user_id)).pack(pady=40)
    tk.Button(dashboard_window, text="Download Ticket", font=("Arial", 35), bg="white", fg="black", command=lambda: open_download_ticket(user_id)).pack(pady=40)
    tk.Button(dashboard_window, text="View Profile", font=("Arial", 35), bg="white", fg="black", command=lambda: view_profile(user_id)).pack(pady=40)
    tk.Button(dashboard_window, text="Payment Methods", font=("Arial", 35), bg="white", fg="black", command=open_payment_methods).pack(pady=40)

    dashboard_window.mainloop()

def open_seat_selection(user_id):
    seat_selection_window = tk.Tk()
    seat_selection_window.title("Seat Selection")
    seat_selection_window.geometry("1900x1700")
    seat_selection_window.configure(bg="lightblue")

    tk.Label(seat_selection_window, text="Select Your Seat", font=("Arial", 60, "bold"), bg="lightblue", fg="black").pack(pady=40)

    seat_frame = tk.Frame(seat_selection_window, bg="#f0f0f0")
    seat_frame.pack(pady=20)

    seats = []
    for row in range(5):
        row_seats = []
        for col in range(5):
            seat = tk.Button(seat_frame, text=f"{row+1}{chr(65+col)}", font=("Arial", 15), bg="white", fg="black", width=4, height=2,
                             command=lambda r=row, c=col: select_seat(r, c, seats))
            seat.grid(row=row, column=col, padx=5, pady=5)
            row_seats.append(seat)
        seats.append(row_seats)

    selected_seat_label = tk.Label(seat_selection_window, text="Selected Seat: None", font=("Arial", 25), bg="#f0f0f0", fg="black")
    selected_seat_label.pack(pady=20)

    bus_no_label = tk.Label(seat_selection_window, text="Bus No:", font=("Arial", 20), bg="#f0f0f0", fg="black")
    bus_no_label.pack(pady=12)
    bus_no_entry = tk.Entry(seat_selection_window, font=("Arial", 20), bg="white", fg="black")
    bus_no_entry.pack(pady=12)

    bus_route_label = tk.Label(seat_selection_window, text="Bus Route (From-To):", font=("Arial", 14), bg="#f0f0f0", fg="black")
    bus_route_label.pack(pady=12)
    bus_route_entry = tk.Entry(seat_selection_window, font=("Arial", 20), bg="white", fg="black")
    bus_route_entry.pack(pady=12)

    date_label = tk.Label(seat_selection_window, text="Date (YYYY-MM-DD):", font=("Arial", 14), bg="#f0f0f0", fg="black")
    date_label.pack(pady=12)
    date_entry = tk.Entry(seat_selection_window, font=("Arial", 20), bg="white", fg="black")
    date_entry.pack(pady=12)

    time_label = tk.Label(seat_selection_window, text="Time (HH:MM):", font=("Arial", 14), bg="#f0f0f0", fg="black")
    time_label.pack(pady=12)
    time_entry = tk.Entry(seat_selection_window, font=("Arial", 20), bg="white", fg="black")
    time_entry.pack(pady=12)

    payment_method_label = tk.Label(seat_selection_window, text="Payment Method:", font=("Arial", 20), bg="#f0f0f0", fg="black")
    payment_method_label.pack(pady=12)
    payment_methods = ["e-Sewa", "Khalti", "Bank Account"]
    selected_payment_method = tk.StringVar(value=payment_methods[0])
    payment_method_menu = tk.OptionMenu(seat_selection_window, selected_payment_method, *payment_methods)
    payment_method_menu.pack(pady=12)

    confirm_button = tk.Button(seat_selection_window, text="Conform Selection", font=("Arial", 20), bg="green", fg="black",
                               command=lambda: confirm_selection(selected_seat_label.cget("text"), user_id, seat_selection_window, bus_no_entry.get(), bus_route_entry.get(), date_entry.get(), time_entry.get(), selected_payment_method.get()))
    confirm_button.pack(pady=12)

    def select_seat(row, col, seats):
        for r in range(5):
            for c in range(5):
                seats[r][c].config(bg="white")  
        seats[row][col].config(bg="lightgreen") 
        selected_seat_label.config(text=f"Selected Seat: {row+1}{chr(65+col)}")

    def confirm_selection(selected_seat, user_id, window, bus_no, bus_route, date, time, payment_method):
        if "None" not in selected_seat:
            seat_number = selected_seat.split(': ')[1]
            passenger_name = simpledialog.askstring("Passenger Name", "Enter Passenger Name:")
            if passenger_name:
                conn = sqlite3.connect('bus_tickets.db')
                c = conn.cursor()
                c.execute("INSERT INTO tickets (user_id, passenger_name, seat_number, bus_no, bus_route, date, time, payment_method) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                          (user_id, passenger_name, seat_number, bus_no, bus_route, date, time, payment_method))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", f"Seat {seat_number} confirmed for {passenger_name}!")
                window.destroy()
            else:
                messagebox.showerror("Error", "Passenger name is required.")
        else:
            messagebox.showerror("Error", "Please select a seat first.")

    seat_selection_window.mainloop()

def open_download_ticket(user_id):
    conn = sqlite3.connect('bus_tickets.db')
    c = conn.cursor()
    c.execute("SELECT passenger_name, seat_number, bus_no, bus_route, date, time, payment_method FROM tickets WHERE user_id=?", (user_id,))
    tickets = c.fetchall()
    conn.close()

    if tickets:
        download_window = tk.Tk()
        download_window.title("Download Ticket")
        download_window.geometry("1900x1700")
        download_window.configure(bg="lightblue")

        tk.Label(download_window, text="Download Your Ticket", font=("Arial", 60, "bold"),fg="black", bg="lightblue").pack(pady=40)

        for ticket in tickets:
            passenger_name, seat_number, bus_no, bus_route, date, time, payment_method = ticket
            tk.Label(download_window, text=f"Passenger Name: {passenger_name}", font=("Arial", 25), fg="black",bg="lightblue").pack(pady=20)
            tk.Label(download_window, text=f"Seat Number: {seat_number}",font=("Arial", 25),fg="black", bg="lightblue").pack(pady=20)
            tk.Label(download_window, text=f"Bus No: {bus_no}",font=("Arial", 25),fg="black", bg="lightblue").pack(pady=20)
            tk.Label(download_window, text=f"Bus Route: {bus_route}",font=("Arial", 25),fg="black", bg="lightblue").pack(pady=20)
            tk.Label(download_window, text=f"Date: {date}",font=("Arial", 25),fg="black", bg="lightblue").pack(pady=20)
            tk.Label(download_window, text=f"Time: {time}",font=("Arial", 25),fg="black", bg="lightblue").pack(pady=20)
            tk.Label(download_window, text=f"Payment Method: {payment_method}",font=("Arial", 25),fg="black", bg="lightblue").pack(pady=20)
            tk.Button(download_window, text="Download Ticket", command=lambda pn=passenger_name, sn=seat_number: download_ticket(pn, sn),font=("Arial", 25),fg="black", bg="lightblue").pack(pady=20)

        download_window.mainloop()
    else:
        messagebox.showinfo("Info", "No tickets found for download.")

def download_ticket(passenger_name, seat_number):
    with open(f"{passenger_name}_ticket.txt", "w") as ticket_file:
        ticket_file.write(f"Passenger Name: {passenger_name}\n")
        ticket_file.write(f"Seat Number: {seat_number}\n")
    messagebox.showinfo("Success", f"Ticket downloaded for {passenger_name}!")

def view_profile(user_id):
    conn = sqlite3.connect('bus_tickets.db')
    c = conn.cursor()
    c.execute("SELECT name, email, contact FROM users WHERE id=?", (user_id,))
    user = c.fetchone()
    conn.close()

    if user:
        profile_window = tk.Tk()
        profile_window.title("Profile")
        profile_window.geometry("1900x1700")
        profile_window.configure(bg="lightblue")

        tk.Label(profile_window, text="Profile", font=("Arial", 60, "bold"), bg="lightblue").pack(pady=40)
        tk.Label(profile_window, text=f"Name: {user[0]}",font=("Arial", 30),fg="black", bg="lightblue").pack(pady=20)
        tk.Label(profile_window, text=f"Email: {user[1]}",font=("Arial", 30),fg="black",bg="lightblue").pack(pady=20)
        tk.Label(profile_window, text=f"Contact: {user[2]}",font=("Arial", 30),fg="black", bg="lightblue").pack(pady=20)

        profile_window.mainloop()
    else:
        messagebox.showerror("Error", "User not found.")

def open_payment_methods():
    payment_window = tk.Tk()
    payment_window.title("Payment Methods")
    payment_window.geometry("1900x1700")
    payment_window.configure(bg="lightblue")

    tk.Label(payment_window, text="Payment Methods", font=("Arial", 60, "bold"), fg="black",bg="lightblue").pack(pady=40)
    tk.Label(payment_window, text="1. e-Sewa", font=("Arial", 30),fg="black", bg="lightblue").pack(pady=20)
    tk.Label(payment_window, text="2. Khalti", font=("Arial", 30), fg="black",bg="lightblue").pack(pady=20)
    tk.Label(payment_window, text="3. Bank Account", font=("Arial", 30),fg="black", bg="lightblue").pack(pady=20)

    payment_window.mainloop()

class ForgetPasswordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Forget Password")
        self.root.geometry("1900x1700")
        self.root.configure(bg='lightblue')

        self.label = tk.Label(root, text="Forget Password", font=("Arial", 60),fg="black", bg='lightblue')
        self.label.pack(pady=40)

        self.question_label = tk.Label(root, text="Security Question:", font=("Arial", 30),fg="black",bg='lightblue')
        self.question_label.pack(pady=20)

        self.questions = [
            "What is your mother's name?",
            "What was the name of your first pet?",
            "What are your hobbies?"
        ]

        self.selected_question = tk.StringVar(value=self.questions[0])
        self.question_menu = tk.OptionMenu(root, self.selected_question, *self.questions)
        self.question_menu.pack(pady=20)

        self.answer_label = tk.Label(root, text="Answer:",font=("Arial", 30),fg="black", bg='lightblue')
        self.answer_label.pack(pady=20)

        self.answer_entry = tk.Entry(root,font=("Arial", 30),fg="black", bg='white')
        self.answer_entry.pack(pady=20)

        self.submit_button = tk.Button(root,font=("Arial", 30),fg="black",text="Submit", command=self.submit_answer)
        self.submit_button.pack(pady=20)

    def submit_answer(self):
        selected_question = self.selected_question.get()
        answer = self.answer_entry.get()

        # Dummy validation for example
        if answer == "":
            messagebox.showwarning("Warning", "Please enter an answer.")
            return

        # Here you would typically check the answer against stored data
        if selected_question == self.questions[0] and answer.lower() == "smith":
            messagebox.showinfo("Success", "Your password is: password123")
        elif selected_question == self.questions[1] and answer.lower() == "fluffy":
            messagebox.showinfo("Success", "Your password is: password123")
        elif selected_question == self.questions[2] and answer.lower() == "new york":
            messagebox.showinfo("Success", "Your password is: password123")
        else:
            messagebox.showerror("Error", "Incorrect answer. Please try again.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sign Up")
    root.geometry("1900x1700")
    root.configure(bg="#eaf7f5")

    left_frame = tk.Frame(root, bg="#2d5d77", width=500, height=350)
    left_frame.pack(side="left", fill="y")
    right_frame = tk.Frame(root, bg="#eaf7f5", width=500, height=350)
    right_frame.pack(side="right", fill="both", expand=True)

    left_frame.grid_propagate(False)
    left_frame.columnconfigure(0, weight=1)
    left_frame.rowconfigure(0, weight=1)
    left_inner_frame = tk.Frame(left_frame, bg="#2d5d77")
    left_inner_frame.grid(sticky="nsew")

    welcome_label = tk.Label(left_inner_frame, text="Welcome Back", font=("Arial", 60, "bold"), bg="#2d5d77", fg="white")
    welcome_label.pack(pady=20)
    create_account_button = tk.Button(left_inner_frame, text="Create Account",bg="blue", fg="black", borderwidth=4, relief="ridge", command=sign_up)
    create_account_button.pack(pady=20)
    login_button = tk.Button(left_inner_frame, text="Login", bg="blue", fg="black", borderwidth=4, relief="ridge", command=login_screen)
    login_button.pack(pady=20)

    right_frame.grid_propagate(False)
    right_frame.columnconfigure(0, weight=1)
    right_frame.rowconfigure(0, weight=1)
    right_inner_frame = tk.Frame(right_frame, bg="#eaf7f5")
    right_inner_frame.grid(sticky="nsew")

    title_label = tk.Label(right_inner_frame, text="Sign Up!", font=("Arial", 60, "bold"), bg="#eaf7f5", fg="black")
    title_label.pack(pady=20)

    fields = [
        ("Name:", tk.Entry(right_inner_frame, width=40)),
        ("Email:", tk.Entry(right_inner_frame, width=40)),
        ("Contact No:", tk.Entry(right_inner_frame, width=40)),
        ("Password:", tk.Entry(right_inner_frame, width=40, show="*"))
    ]

    for label_text, entry_widget in fields:
        label = tk.Label(right_inner_frame, text=label_text, bg="#eaf7f5", fg="black")
        label.pack(pady=2)
        entry_widget.pack(pady=2)

    sign_up_button = tk.Button(right_inner_frame, text="Sign Up", command=sign_up, bg="white", fg="black", width=20, borderwidth=2, relief="ridge")
    sign_up_button.pack(pady=30)

    initialize_db()
    root.mainloop()   