import tkinter as tk
from tkinter import messagebox

class BusTicketBooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Bus Ticket Booking System")
        self.root.geometry("400x500")
        self.root.configure(bg="light blue")

        self.seats = [[0 for _ in range(4)] for _ in range(5)]  # 5 rows x 4 columns
        self.buttons = []

        tk.Label(self.root, text="Select Your Seats", font=("Arial", 14, "bold"), bg="light blue").pack(pady=10)
        
        self.seat_frame = tk.Frame(self.root, bg="light blue")
        self.seat_frame.pack()
        
        self.routes = ["Route 1", "Route 2", "Route 3", "Route 4"]
        self.route_var = tk.StringVar(self.root)
        self.route_var.set(self.routes[0])
        
        tk.Label(self.root, text="Select Route", font=("Arial", 12), bg="light blue").pack(pady=5)
        tk.OptionMenu(self.root, self.route_var, *self.routes).pack(pady=5)
        
        seat_labels = [[f"A{i*4 + j + 1}" for j in range(4)] for i in range(5)]
        
        for i in range(5):
            row_buttons = []
            for j in range(4):
                btn = tk.Button(
                    self.seat_frame, text=seat_labels[i][j], width=5, height=2,
                    command=lambda r=i, c=j: self.select_seat(r, c)
                )
                btn.grid(row=i, column=j, padx=5, pady=5)
                row_buttons.append(btn)
            self.buttons.append(row_buttons)

        self.confirm_button = tk.Button(self.root, text="Conform Booking", command=self.confirm_booking, state=tk.DISABLED)
        self.confirm_button.pack(pady=20)

        self.selected_seats = []

    def select_seat(self, row, col):
        if self.seats[row][col] == 0:
            self.seats[row][col] = 1
            self.buttons[row][col].config(bg="green")
            self.selected_seats.append((row, col))
        else:
            self.seats[row][col] = 0
            self.buttons[row][col].config(bg="SystemButtonFace")
            self.selected_seats.remove((row, col))
        
        self.confirm_button.config(state=tk.NORMAL if self.selected_seats else tk.DISABLED)
    
    def confirm_booking(self):
        if self.selected_seats:
            seat_numbers = [f"A{r * 4 + c + 1}" for r, c in self.selected_seats]
            selected_route = self.route_var.get()
            messagebox.showinfo("Booking Conformed", f"Route: {selected_route}\nSeats booked: {', '.join(seat_numbers)}")
            for r, c in self.selected_seats:
                self.buttons[r][c].config(bg="gray", state=tk.DISABLED)
            self.selected_seats.clear()
            self.confirm_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = BusTicketBooking(root)
    root.mainloop()
