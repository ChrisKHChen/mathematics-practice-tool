import tkinter as tk
from tkinter import messagebox
from quiz_logic import QuizLogic

class QuizScreen:
    def __init__(self, master, difficulty, question_amount):
        self.master = master

        self.difficulty = difficulty
        self.question_amount = question_amount
        self.score = 0
        self.current_question_index = 0
        self.questions = []

        self.logic = QuizLogic(difficulty, question_amount)
        self.logic.generate_questions()
        self.setup_ui()


    def setup_ui(self):
        self.frame = tk.Frame(self.master)
        self.frame.pack(pady=200)

        # [Label] Question Indicator (1/15)
        self.question_count_label = tk.Label(self.frame, text="", font=("Arial", 20))
        self.question_count_label.pack(anchor='nw', pady=50)

        # [Label] Math Question
        self.question_label = tk.Label(self.frame, text="", font=("Arial", 32))
        self.question_label.pack()

        # [Input] Answer Field
        self.answer_entry = tk.Entry(self.frame, width=20, font=("Arial", 24))
        self.answer_entry.pack(pady=30)

        # [Keybind] 'ENTER' Submit Answer
        self.answer_entry.bind("<Return>", lambda event: self.submit_answer())

        # [Button] Submit Answer
        self.submit_button = tk.Button(self.frame, text="Submit Answer", command=self.submit_answer, font=("Arial", 24))
        self.submit_button.pack(pady=30)

        # [Label] Current Score
        self.score_label = tk.Label(self.frame, text=f"Score: {self.score}", font=("Arial", 24))
        self.score_label.pack()

        self.load_question()


    def load_question(self):
        if self.current_question_index < self.question_amount:
            question = self.logic.questions[self.current_question_index]
            self.question_label.config(text=question)
            self.update_question_count()
        else:
            self.end_quiz()


    def update_question_count(self):
        self.question_count_label.config(text=f"Question: {self.current_question_index + 1}/{self.question_amount}")


    def submit_answer(self):
        user_input = self.answer_entry.get()
        # Handle empty answer field.
        if not user_input:
            messagebox.showwarning("Input Error", "Please enter an answer before submitting.")
            return
        # Handle non-integer in answer field.
        try:
            user_answer = int(user_input)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number.")
            return

        correct_answer = self.logic.get_correct_answer(self.current_question_index)
        if user_answer == correct_answer:
            self.score += 1

        self.current_question_index += 1
        self.answer_entry.delete(0, tk.END)
        self.score_label.config(text=f"Score: {self.score}")
        self.load_question()


    def end_quiz(self):
        self.frame.destroy()
        result_label = tk.Label(self.master, text=f"Quiz Finished! Your score: {self.score}/{self.question_amount}", font=("Helvetica", 16))
        result_label.pack(pady=20)