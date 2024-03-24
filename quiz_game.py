import tkinter as tk

class QuizApp(tk.Tk):
    def __init__(self): 
        super().__init__()
        self.title("Quiz Game")
        self.geometry("600x400")
        self.current_slide = 0
        self.score = 0
        self.questions = [
            {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Rome"], "correct": 0},
            {"question": "Who wrote 'Hamlet'?", "options": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Leo Tolstoy"], "correct": 0},
            {"question": "What is the largest mammal?", "options": ["Elephant", "Whale", "Giraffe", "Rhino"], "correct": 1}
        ]

        self.create_widgets()

    def create_widgets(self):
        self.question_label = tk.Label(self, text="", font=("Helvetica", 16))
        self.question_label.pack(pady=10)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self, text="", command=lambda idx=i: self.check_answer(idx), font=("Helvetica", 12), state=tk.DISABLED)
            button.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)
            self.option_buttons.append(button)

        self.feedback_label = tk.Label(self, text="", font=("Helvetica", 12))
        self.feedback_label.pack(pady=10)

        self.previous_button = tk.Button(self, text="Previous", command=self.previous_slide, font=("Helvetica", 14), state=tk.DISABLED)
        self.previous_button.pack(pady=10)

        self.next_button = tk.Button(self, text="Next", command=self.next_slide, font=("Helvetica", 14))
        self.next_button.pack(pady=10)

        self.show_slide()

    def show_slide(self):
        slide = self.questions[self.current_slide]
        self.question_label.config(text=slide['question'])

        for i, option in enumerate(slide['options']):
            self.option_buttons[i].config(text=option, state=tk.NORMAL)

        self.update_score_label()

        for button in self.option_buttons:
            button.config(state=tk.NORMAL)

        self.previous_button.config(state=tk.NORMAL)

        if self.current_slide == 0:
            self.previous_button.config(state=tk.DISABLED)

    def check_answer(self, idx):
        slide = self.questions[self.current_slide]
        if idx == slide['correct']:
            self.feedback_label.config(text="Correct!", fg="green")
            self.score += 1
        else:
            self.feedback_label.config(text="Incorrect!", fg="red")

        self.update_score_label()

        for button in self.option_buttons[idx:]:
            button.config(state=tk.DISABLED)

    def update_score_label(self):
        self.feedback_label.config(text=f"Score: {self.score}/{len(self.questions)}")

    def previous_slide(self):
        if self.current_slide > 0:
           self.current_slide -= 1
           self.show_slide()

    def next_slide(self):
        self.current_slide += 1
        if self.current_slide < len(self.questions):
            self.show_slide()
        else:
            self.show_scorecard()

    def show_scorecard(self):
        self.question_label.config(text="Quiz Completed!", font=("Helvetica", 16))
        self.feedback_label.config(text=f"Your score: {self.score}/{len(self.questions)}", fg="blue")
        self.next_button.config(state="disabled")
        self.previous_button.config(state="disabled")
        for button in self.option_buttons:
            button.config(state="disabled")

if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()
