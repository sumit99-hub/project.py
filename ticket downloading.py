import tkinter as tk
from tkinter import messagebox

class BusTicketBookingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Bus Ticket Booking System")
        self.root.geometry("400x400")
        self.root.configure(bg="lightblue")

        # Passenger details
        self.passenger_name_label = tk.Label(root, text="Passenger Name:", bg="lightblue")
        self.passenger_name_label.pack(pady=10)
        self.passenger_name_entry = tk.Entry(root)
        self.passenger_name_entry.pack(pady=10)

        self.passenger_seat_label = tk.Label(root, text="Seat Number:", bg="lightblue")
        self.passenger_seat_label.pack(pady=10)
        self.passenger_seat_entry = tk.Entry(root)
        self.passenger_seat_entry.pack(pady=10)

        # Booking button
        self.book_button = tk.Button(root, text="Your ticket is booked", command=self.book_ticket)
        self.book_button.pack(pady=20)

        # Download button
        self.download_button = tk.Button(root, text="Download Your Ticket", command=self.download_ticket)
        self.download_button.pack(pady=20)

    def book_ticket(self):
        name = self.passenger_name_entry.get()
        age = self.passenger_age_entry.get()
        seat = self.passenger_seat_entry.get()

        if name and age and seat:
            messagebox.showinfo("Success", f"Ticket booked for {name} (Age: {age}) at Seat: {seat}")
        else:
            messagebox.showerror("Error", "Please fill all fields")

    def download_ticket(self):
        name = self.passenger_name_entry.get()
        seat = self.passenger_seat_entry.get()

        if name and seat:
            with open(f"{name}_ticket.txt", "w") as ticket_file:
                ticket_file.write(f"Passenger Name: {name}\n")
                
                ticket_file.write(f"Seat Number: {seat}\n")
            messagebox.showinfo("Success", f"Ticket downloaded for {name}!")
        else:
            messagebox.showerror("Error", "Please fill all fields")

if __name__ == "__main__":
    root = tk.Tk()
    app = BusTicketBookingSystem(root)
    root.mainloop()
