import tkinter as tk
from tkinter import messagebox

class BusTicketBookingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Bus Ticket Booking System")
        self.root.geometry("400x400")
        self.root.config(bg="lightblue")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Payment Method Services", bg="lightblue", font=("Helvetica", 16)).pack(pady=10)

        tk.Label(self.root, text="Select Payment Method", bg="lightblue",fg="black").pack(pady=10)

        self.payment_method = tk.StringVar(value="None")

        tk.Radiobutton(self.root, text="e-Sewa", variable=self.payment_method, value="e-Sewa", bg="lightblue").pack(anchor=tk.W)
        tk.Radiobutton(self.root, text="Khalti", variable=self.payment_method, value="Khelti", bg="lightblue").pack(anchor=tk.W)
        tk.Radiobutton(self.root, text="Credit/Debit Card", variable=self.payment_method, value="Card", bg="lightblue").pack(anchor=tk.W)
        tk.Radiobutton(self.root, text="Bank Account", variable=self.payment_method, value="Bank Account", bg="lightblue").pack(anchor=tk.W)

        tk.Button(self.root, text="Conform Payment", command=self.confirm_payment, bg="lightgray").pack(pady=20)

    def confirm_payment(self):
        payment_option = self.payment_method.get()
        if payment_option != "None":
            messagebox.showinfo("Payment Conformation", f"You have selected {payment_option} for payment.")
        else:
            messagebox.showwarning("Warning", "Please select a payment method.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BusTicketBookingSystem(root)
    root.mainloop()
