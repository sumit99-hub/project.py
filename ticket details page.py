import tkinter as tk
from tkinter import messagebox

def book_ticket():
    bus_name = bus_name_entry.get()
    from_location = from_entry.get()
    to_location = to_entry.get()
    departure_date = date_entry.get()
    departure_time = time_entry.get()
    
    if bus_name and from_location and to_location and departure_date and departure_time:
        messagebox.showinfo("Success", f"Ticket booked successfully!\n\nBus: {bus_name}\nFrom: {from_location}\nTo: {to_location}\nDate: {departure_date}\nTime: {departure_time}")
    else:
        messagebox.showerror("Error", "All fields are required!")

# Create main window
root = tk.Tk()
root.title("Bus Ticket Booking")
root.geometry("400x400")
root.configure(bg="#87CEEB")  # Light blue background

# Labels and Entries
tk.Label(root, text="Bus Ticket Details", font=("Arial", 16, "bold"), fg="white", bg="blue").pack(pady=10)

tk.Label(root, text="Bus Name:", bg="#87CEEB", font=("Arial", 12)).pack()
bus_name_entry = tk.Entry(root, width=30)
bus_name_entry.pack()

tk.Label(root, text="From:", bg="#87CEEB", font=("Arial", 12)).pack()
from_entry = tk.Entry(root, width=30)
from_entry.pack()

tk.Label(root, text="To:", bg="#87CEEB", font=("Arial", 12)).pack()
to_entry = tk.Entry(root, width=30)
to_entry.pack()

tk.Label(root, text="Departure Date (DD-MM-YYYY):", bg="#87CEEB", font=("Arial", 12)).pack()
date_entry = tk.Entry(root, width=30)
date_entry.pack()

tk.Label(root, text="Departure Time (HH:MM):", bg="#87CEEB", font=("Arial", 12)).pack()
time_entry = tk.Entry(root, width=30)
time_entry.pack()

# Submit Button
book_button = tk.Button(root, text="Book Ticket", font=("Arial", 12, "bold"), fg="white", bg="blue", command=book_ticket)
book_button.pack(pady=10)

root.mainloop()
