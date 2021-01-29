from tkinter import *
from AskMeClass import AskMe


transx = -0.05
transy = 0.0


root = Tk()
root.title('Ask Me')


def search_question():
    question = search.get(1.0, 'end')
    bot = AskMe(question)
    bot_answer = bot.answer
    print(bot_answer)
    answer_text.config(state=NORMAL)
    answer_text.insert(1.0, bot_answer)
    answer_text.config(state=DISABLED)


def reset():
    search.delete(1.0, END)
    answer_text.config(state=NORMAL)
    answer_text.delete(1.0, END)


canvas = Canvas(root, width=900, height=900, bg="#ececec")
canvas.pack()

question = Label(canvas, text="Question:", bg="#ececec", font="Helvetica 24 bold")
question.place(relx=transx + 0.1, rely=transy + 0.2, relwidth=0.15, relheight=0.1)

search = Text(canvas, font="Helvetica 18 bold")
search.place(relx=transx + 0.27, rely=transy + 0.225, relwidth=0.5, relheight=0.05)

search_button = Button(canvas, text="Enter", font="Helvetica 24 bold", command=lambda: search_question())
search_button.place(relx=transx + 0.8, rely=transy + 0.225, relwidth=0.15, relheight=0.05)

answer = Label(canvas, text="Answer:", bg="#ececec", font="Helvetica 24 bold")
answer.place(relx=transx + 0.09, rely=transy + 0.36, relwidth=0.15, relheight=0.1)

answer_text = Text(canvas, bd=3, font="Helvetica 18 bold")
answer_text.place(relx=transx + 0.27, rely=transy + 0.4, relwidth=0.5, relheight=0.5)

reset_button = Button(canvas, text="Reset", font="Helvetica 24 bold", command=lambda: reset())
reset_button.place(relx=transx + 0.8, rely=transy + 0.85, relwidth=0.15, relheight=0.05)

root.mainloop()
