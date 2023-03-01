from tkinter import *
from data import question_list, answers_list

# Základní barvy pozadí a tlačítek
bg_color = "#E8D2A6"
next_color = "#86A3B8"
quit_color = "#F55050"


Score = 0
Total_no_questions = len(question_list)
Question_no = 1

# Spustí stejný kvíz znovu
def start_again():
    global Score, Question_no
    Score = 0
    Question_no = 1
    val1.set(0)
    val2.set(0)
    question.config(text=question_list[Question_no-1])

    play_again.place_forget()
    score.place_forget()
    quit_button.place_forget()
    root.pack()

# ukončí program (zavře okno)
def window_destroy():
    window.destroy()

# nastaví další otázku kvízu
def next():
    global Score, Question_no
    if val1.get() == 1:
        selected_option = "True"

    elif val2.get() == 1:
        selected_option = "False"

    else:
        selected_option = ""

    if answers_list[Question_no - 1] == selected_option:
        Score += 1

    Question_no += 1

    if Question_no > Total_no_questions:
        root.pack_forget()
        score.place(relx=.45, rely=.3)
        play_again.place(rely=0.6, relx=0.3, width=80)
        quit_button.place(rely=0.6, relx=0.6, width=80)
        score.config(text=f"Score: {Score}/{Total_no_questions}")
    else:
        val1.set(0)
        val2.set(0)
        question.config(text=question_list[Question_no-1])

# Vyhodnotí odpověď uživatele
def check(option):
    if option == 1:
        val2.set(0)
    else:
        val1.set(0)

# Shodí úvodní frame - objeví se kvíz
def start_game():
    start_screen.place_forget()
    root.pack()

# Základní rozložení jednotlivých částí kvízu
window = Tk()
window.geometry("750x200")
window.title("Quiz game")
window.config(bg=bg_color)

start_screen = Frame(bg=bg_color)
start_screen.place(relx=.5, rely=.5, anchor=CENTER)

intro_text = Label(start_screen, text="Let´s play Quiz Game!", font=("Arial", 15), bg=bg_color)
intro_text.pack(pady=(0,20))

play_b = Button(start_screen, text="Play Game", bg=next_color, command=start_game)
play_b.pack()

root = Frame(bg=bg_color)
root.pack_forget()

question = Message(root, width=560, font=("Arial", 13), text=question_list[0], justify=CENTER, bg=bg_color)
question.pack(pady=(20, 10))

val1 = IntVar()
val2 = IntVar()

option1 = Checkbutton(root, variable=val1, text="True", bg=bg_color, font=("Arial", 11), command=lambda: check(1))
option1.pack()

option2 = Checkbutton(root, variable=val2, text="False", bg=bg_color, font=("Arial", 11), command=lambda: check(2))
option2.pack()

next_b = Button(root, text="next", font=("Arial", 10),width=10, bg=next_color, command=next)
next_b.pack(pady=20)

# Konec kvízu - skore, hrát znovu, quit
score = Label(window, font=("Arial", 14), bg=bg_color)
score.place_forget()

play_again = Button(window, text="Play Again", command=start_again, bg=next_color)
play_again.place_forget()

quit_button = Button(window, text="Quit", bg=quit_color, command=window_destroy)
quit_button.place_forget()

window.mainloop()