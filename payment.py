import tkinter as tk
from tkinter import messagebox
import sqlite3

def initialize_db():
    conn = sqlite3.connect('payment.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS payment
                 (e_Sewa TEXT NOT NULL UNIQUE,
                  Khalti TEXT NOT NULL,
                  Card TEXT NOT NULL,
                  Bank_Account TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def insert_payment_method(e_Sewa, Khalti, Card, Bank_Account):
    conn = sqlite3.connect('payment.db')
    c = conn.cursor()
    c.execute("INSERT INTO payment (e_Sewa, Khalti, Card, Bank_Account) VALUES (?, ?, ?, ?)",
              (e_Sewa, Khalti, Card, Bank_Account))
    conn.commit()
    conn.close()

def get_payment_method():
    conn = sqlite3.connect('payment.db')
    c = conn.cursor()
    c.execute("SELECT * FROM payment")
    payment_methods = c.fetchall()
    conn.close()
    return payment_methods      

def update_payment_method(e_Sewa, Khalti, Card, Bank_Account):
    conn = sqlite3.connect('payment.db')
    c = conn.cursor()
    c.execute("UPDATE payment SET e_Sewa = ?, Khalti = ?, Card = ?, Bank_Account = ?",
              (e_Sewa, Khalti, Card, Bank_Account))
    conn.commit()
    conn.close()

def delete_payment_method():
    conn = sqlite3.connect('payment.db')
    c = conn.cursor()
    c.execute("DELETE FROM payment")
    conn.commit()
    conn.close()        

    

class BusTicketBookingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Bus Ticket Booking System")
        self.root.geometry("400x400")
        self.root.config(bg="lightblue")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Payment Method Services", bg="lightblue", font=("Helvetica", 16)).pack(pady=10)

        tk.Label(self.root, text="Select Payment Method", bg="lightblue", fg="black").pack(pady=10)

        self.payment_method = tk.StringVar(value="None")

        tk.Radiobutton(self.root, text="e-Sewa", variable=self.payment_method, value="e-Sewa", bg="lightblue").pack(anchor=tk.W)
        tk.Radiobutton(self.root, text="Khalti", variable=self.payment_method, value="Khalti", bg="lightblue").pack(anchor=tk.W)
        tk.Radiobutton(self.root, text="Credit/Debit Card", variable=self.payment_method, value="Card", bg="lightblue").pack(anchor=tk.W)
        tk.Radiobutton(self.root, text="Bank Account", variable=self.payment_method, value="Bank Account", bg="lightblue").pack(anchor=tk.W)

        tk.Button(self.root, text="Confirm Payment", command=self.confirm_payment, bg="lightgray").pack(pady=20)

    def confirm_payment(self):
        payment_option = self.payment_method.get()
        if payment_option != "None":
            messagebox.showinfo("Payment Confirmation", f"You have selected {payment_option} for payment.")
        else:
            messagebox.showwarning("Warning", "Please select a payment method.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BusTicketBookingSystem(root)
    initialize_db()
    root.mainloop()