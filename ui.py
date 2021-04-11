from tkinter import *
from quiz_brain import QuizBrain




THEME_COLOR = "#375362"




class QuizeInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # self.check_answer = check_answer
        # self.score = score

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.title_score = Label(text=f"Score: {0}", bg=THEME_COLOR, foreground="white")
        self.title_score.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,125,
            width=280,
            text="Some text",fill=THEME_COLOR,
            font=("Ariel",20,"italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)


        self.wrong_image = PhotoImage(file="false.png")
        self.wrong = Button(image=self.wrong_image, width=80, height=80, highlightthickness=0, command = self.false_pressed)
        self.wrong.grid(row=2, column=1)

        self.correct_image = PhotoImage(file="true.png")
        self.correct_button = Button(image=self.correct_image, width=80, height=80, highlightthickness=0,command=self.true_pressed)
        self.correct_button.grid(row=2, column=0)

        self.get_next_question()


        self.window.mainloop()





    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.title_score.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text = f"You have reached the end of the quize. your final score is : {self.quiz.score}")
            self.wrong.config(state="disabled")
            self.correct_button.config(state="disabled")



    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))




    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
















