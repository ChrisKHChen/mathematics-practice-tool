import tkinter as tk
from quiz_screen import QuizScreen

class StartScreen:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)
        self.frame.pack(pady=50)

        # [Label] Welcome Message
        self.label = tk.Label(self.frame, text="Welcome to the Math Quiz!", font=("Arial", 40))
        self.label.pack()

        # [Label] Difficulty Text
        self.difficulty_label = tk.Label(self.frame, text="Select Difficulty:", font=("Arial", 30))
        self.difficulty_label.pack(pady=20)

        # [Radio Button] Difficulty Selector
        self.difficulty_var = tk.StringVar(value="easy")
        self.easy_rb = tk.Radiobutton(self.frame, text="Easy", variable=self.difficulty_var, value="easy", font=("Arial", 20))
        self.medium_rb = tk.Radiobutton(self.frame, text="Medium", variable=self.difficulty_var, value="medium", font=("Arial", 20))
        self.hard_rb = tk.Radiobutton(self.frame, text="Hard", variable=self.difficulty_var, value="hard", font=("Arial", 20))
        self.easy_rb.pack(anchor=tk.W, padx=220)
        self.medium_rb.pack(anchor=tk.W, padx=220)
        self.hard_rb.pack(anchor=tk.W, padx=220)

        # [Label] Question Amount Text
        self.question_amount_label = tk.Label(self.frame, text="Select Number of Questions:", font=("Arial", 30))
        self.question_amount_label.pack(pady=20)

        # [Radio Button] Question Amount Selector
        self.question_amount_var = tk.StringVar(value="5")
        self.q5_rb = tk.Radiobutton(self.frame, text="5 Questions", variable=self.question_amount_var, value="5", font=("Arial", 20))
        self.q10_rb = tk.Radiobutton(self.frame, text="10 Questions", variable=self.question_amount_var, value="10", font=("Arial", 20))
        self.q20_rb = tk.Radiobutton(self.frame, text="20 Questions", variable=self.question_amount_var, value="20", font=("Arial", 20))
        self.q5_rb.pack(anchor=tk.W, padx=220)
        self.q10_rb.pack(anchor=tk.W, padx=220)
        self.q20_rb.pack(anchor=tk.W, padx=220)

        # [Button] Start Quiz
        self.start_button = tk.Button(self.frame, text="Start Quiz", command=self.start_quiz, font=("Arial", 32))
        self.start_button.pack(pady=50)


    def start_quiz(self):
        difficulty = self.difficulty_var.get()
        question_amount = int(self.question_amount_var.get())
        self.frame.destroy()
        QuizScreen(self.master, difficulty, question_amount)