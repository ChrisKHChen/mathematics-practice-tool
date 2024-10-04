import random

class QuizLogic:
    def __init__(self, difficulty, question_amount):
        self.difficulty = difficulty
        self.question_amount = question_amount
        self.questions = []
        self.answers = []


    def generate_questions(self):
        for _ in range(self.question_amount):
            question, answer = self.create_question()
            self.questions.append(question)
            self.answers.append(answer)


    def create_question(self):
        if self.difficulty == 'easy':
            return self.create_easy_question()
        elif self.difficulty == 'medium':
            return self.create_medium_question()
        else:
            return self.create_hard_question()


    def create_easy_question(self):
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        operation = random.choice(['+', '-', '*', '/'])
        question = f"{num1} {operation} {num2}"

        # Make sure division results in whole number.
        if operation == '/':
            num1 = num1 * num2
            question = f"{num1} {operation} {num2}"

        answer = self.perform_operation(num1, num2, operation)
        return question, answer


    def create_medium_question(self):
        num1 = random.randint(-50, 50)
        num2 = random.randint(-50, 50)
        num3 = random.randint(-50, 50)
        operation1 = random.choice(['+', '-', '*'])
        operation2 = random.choice(['+', '-', '*'])
        question = f"({num1} {operation1} {num2}) {operation2} {num3}"

        result1 = self.perform_operation(num1, num2, operation1)
        answer = self.perform_operation(result1, num3, operation2)
        return question, answer


    def create_hard_question(self):
        num1 = random.randint(0, 100)
        num2 = random.randint(1, 100)
        num3 = random.randint(0, 100)
        operation1 = random.choice(['+', '-', '*', '/'])
        operation2 = random.choice(['+', '-', '*'])
        question = f"({num1} {operation1} {num2}) {operation2} {num3}"

        # Make sure division results in whole number.
        if operation1 == '/':
            num1 = num1 * num2
            question = f"({num1} {operation1} {num2}) {operation2} {num3}"

        result1 = self.perform_operation(num1, num2, operation1)
        answer = self.perform_operation(result1, num3, operation2)
        return question, answer


    def perform_operation(self, num1, num2, operation):
        operations = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b
        }
        return operations.get(operation, lambda a, b: None)(num1, num2)


    def get_correct_answer(self, index):
        return self.answers[index]