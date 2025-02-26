import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Thank You", "Thank You For Visiting Here")

def main():
    root = tk.Tk()
    root.title("Bus Ticket Booking")
    
    # Set the background color
    root.configure(bg='lightblue')

    # Set the window size
    root.geometry("400x400")

    # Add a label for the title
    title_label = tk.Label(root, text="Ticket Conformation  ", font=("Helvetica", 16, "bold"), bg='lightblue', fg='black')
    title_label.pack(pady=20)

    # Add a button to show the thank you message
    thank_you_button = tk.Button(root, text="Your ticket has been booked", font=("Helvetica", 14), bg='blue', fg='black', command=show_message)
    thank_you_button.pack(pady=20)

    # Add a congratulation letter message
    congrats_label = tk.Label(root, text="Congratulations on Booking Your Ticket!", font=("Helvetica", 14), bg='lightblue', fg='black')
    congrats_label.pack(pady=20)

    # Start the main loop
    root.mainloop()

if __name__ == "__main__":
    main()
