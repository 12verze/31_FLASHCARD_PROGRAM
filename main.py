from tkinter import *

import pandas
from pandas import *
from random import *

BACKGROUND_COLOR = "#B1DDC6"
clicks =0
new_word = {}

try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("french_words.csv")
    word_dict = data.to_dict(orient="records")
else:
    word_dict = data.to_dict(orient="records")



def word_update():
    global clicks, front, back, timer
    global new_word
    window.after_cancel(timer)
    new_word = choice(word_dict)
    canvas.itemconfig(card_word,text=new_word["French"],fill="black")
    canvas.itemconfig(card_title,text="French",fill="black")
    #front = PhotoImage(file="card_front.png")
    canvas.itemconfig(card_image,image = front)
    timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_word, text=new_word["English"],fill="white")
    canvas.itemconfig(card_title, text="English",fill="white")
    # back = PhotoImage(file="card_back.png")
    canvas.itemconfig(card_image, image=back)


def is_known():
    word_dict.remove(new_word)
    word_update()
    data_word = pandas.DataFrame(word_dict)
    data_word.to_csv("words_to_learn.csv",index=False)


window = Tk()
window.title("FLASHY")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000,func=flip_card)

canvas = Canvas(width = 800, height = 526,bg =BACKGROUND_COLOR,highlightthickness=0)
front = PhotoImage(file="card_front.png")
back = PhotoImage(file = "card_back.png")
card_image = canvas.create_image(400,263,image= front)
card_title =canvas.create_text(400,150,text="Title",font=("Serif",30,"italic"))
card_word = canvas.create_text(400,263,text="word",font=("Times New Roman",50,"bold"))

canvas.grid(column=0,row=0,columnspan=2)

cross_image = PhotoImage(file="wrong.png")
cross = Button(image=cross_image,highlightthickness=0,bg=BACKGROUND_COLOR,command=word_update)
cross.grid(column=0, row = 1)

right_image = PhotoImage(file="right.png")
right = Button(image=right_image,highlightthickness=0,bg=BACKGROUND_COLOR,command=is_known)
right.grid(column=1, row = 1)


word_update()


window.mainloop()







