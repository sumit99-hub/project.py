import tkinter as tk
from tkinter import messagebox

class ForgetPasswordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Forget Password")
        self.root.geometry("400x400")
        self.root.configure(bg='lightblue')

        self.label = tk.Label(root, text="Forget Password", font=("Arial", 16), bg='lightblue')
        self.label.pack(pady=10)

        self.question_label = tk.Label(root, text="Security Question:", bg='lightblue')
        self.question_label.pack(pady=5)

        self.questions = [
            "What is your mother's name?",
            "What was the name of your first pet?",
            "What are your hobbies?"
        ]

        self.selected_question = tk.StringVar(value=self.questions[0])
        self.question_menu = tk.OptionMenu(root, self.selected_question, *self.questions)
        self.question_menu.pack(pady=5)

        self.answer_label = tk.Label(root, text="Answer:", bg='lightblue')
        self.answer_label.pack(pady=5)

        self.answer_entry = tk.Entry(root, bg='white')
        self.answer_entry.pack(pady=5)

        self.submit_button = tk.Button(root, text="Submit", command=self.submit_answer)
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
    app = ForgetPasswordApp(root)
    root.mainloop()
