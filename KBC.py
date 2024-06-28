import tkinter as tk
from tkinter import messagebox, font
import random

questions = [
    ["What is the capital of France?", "Berlin", "Madrid", "Paris", "Lisbon", 3],
    [
        "Which planet is known as the Red Planet?",
        "Earth",
        "Mars",
        "Jupiter",
        "Venus",
        2,
    ],
    [
        "What is the largest mammal?",
        "Elephant",
        "Blue Whale",
        "Giraffe",
        "Great White Shark",
        2,
    ],
    [
        "Which element has the chemical symbol 'O'?",
        "Oxygen",
        "Gold",
        "Osmium",
        "Iron",
        1,
    ],
    [
        "Who wrote 'Hamlet'?",
        "Charles Dickens",
        "William Shakespeare",
        "Mark Twain",
        "J.K. Rowling",
        2,
    ],
    [
        "What is the hardest natural substance on Earth?",
        "Gold",
        "Iron",
        "Diamond",
        "Platinum",
        3,
    ],
    ["In which year did the Titanic sink?", "1905", "1912", "1923", "1945", 2],
    [
        "Which continent is known as the 'Dark Continent'?",
        "Asia",
        "Australia",
        "Africa",
        "Europe",
        3,
    ],
    ["What is the square root of 64?", "6", "7", "8", "9", 3],
    ["Which is the smallest prime number?", "0", "1", "2", "3", 3],
]

levels = [1000, 2000, 3000, 4000, 5000, 10000, 20000, 40000, 80000, 160000]
money = 0
current_question = 0
time_left = 30
timer_id = None


def check_answer(answer):
    global current_question, money, timer_id

    if answer == questions[current_question][5]:
        messagebox.showinfo(
            "Correct!", f"Correct answer! You've won ₹{levels[current_question]}!"
        )
        money = levels[current_question]
        current_question += 1
        if current_question < len(questions):
            load_question()
        else:
            messagebox.showinfo(
                "Congratulations!", f"You've won the grand prize of ₹{money}!"
            )
            root.quit()
    else:
        messagebox.showerror("Wrong!", f"Wrong answer! You take home ₹{money}")
        root.quit()

    if timer_id:
        root.after_cancel(timer_id)


def load_question():
    global time_left, timer_id
    question = questions[current_question]
    question_label.config(
        text=f"Question for ₹{levels[current_question]}:\n{question[0]}"
    )

    options = list(enumerate(question[1:5], 1))
    random.shuffle(options)

    button_a.config(
        text=f"{options[0][0]}. {options[0][1]}",
        command=lambda: check_answer(options[0][0]),
        state=tk.NORMAL,
    )
    button_b.config(
        text=f"{options[1][0]}. {options[1][1]}",
        command=lambda: check_answer(options[1][0]),
        state=tk.NORMAL,
    )
    button_c.config(
        text=f"{options[2][0]}. {options[2][1]}",
        command=lambda: check_answer(options[2][0]),
        state=tk.NORMAL,
    )
    button_d.config(
        text=f"{options[3][0]}. {options[3][1]}",
        command=lambda: check_answer(options[3][0]),
        state=tk.NORMAL,
    )

    level_label.config(text=f"Level: {current_question + 1}")
    money_label.config(text=f"Current Money: ₹{money}")

    time_left = 30
    update_timer()

    if current_question == 0:
        lifeline_button.config(state=tk.NORMAL)


def update_timer():
    global time_left, timer_id
    timer_label.config(text=f"Time left: {time_left} seconds")
    if time_left > 0:
        time_left -= 1
        timer_id = root.after(1000, update_timer)
    else:
        messagebox.showwarning(
            "Time's up!", f"You've run out of time! You take home ₹{money}"
        )
        root.quit()


def use_lifeline():
    correct_answer = questions[current_question][5]
    wrong_answers = [i for i in range(1, 5) if i != correct_answer]
    remove = random.sample(wrong_answers, 2)

    for button in [button_a, button_b, button_c, button_d]:
        button_answer = int(button.cget("text").split(".")[0])
        if button_answer in remove:
            button.config(state=tk.DISABLED)

    lifeline_button.config(state=tk.DISABLED)


root = tk.Tk()
root.title("Colorful Quiz Game")
root.geometry("700x500")
root.configure(bg="#2C3E50")

title_font = font.Font(family="Helvetica", size=24, weight="bold")
question_font = font.Font(family="Helvetica", size=16)
button_font = font.Font(family="Helvetica", size=14)
label_font = font.Font(family="Helvetica", size=12)

title_label = tk.Label(
    root, text="Quiz Master", font=title_font, bg="#2C3E50", fg="#ECF0F1"
)
title_label.pack(pady=20)

question_label = tk.Label(
    root,
    text="",
    font=question_font,
    wraplength=600,
    justify="center",
    bg="#2C3E50",
    fg="#ECF0F1",
)
question_label.pack(pady=20)

button_frame = tk.Frame(root, bg="#2C3E50")
button_frame.pack(pady=10)

button_a = tk.Button(
    button_frame,
    text="",
    font=button_font,
    width=30,
    bg="#3498DB",
    fg="white",
    activebackground="#2980B9",
)
button_a.grid(row=0, column=0, padx=5, pady=5)

button_b = tk.Button(
    button_frame,
    text="",
    font=button_font,
    width=30,
    bg="#2ECC71",
    fg="white",
    activebackground="#27AE60",
)
button_b.grid(row=0, column=1, padx=5, pady=5)

button_c = tk.Button(
    button_frame,
    text="",
    font=button_font,
    width=30,
    bg="#E74C3C",
    fg="white",
    activebackground="#C0392B",
)
button_c.grid(row=1, column=0, padx=5, pady=5)

button_d = tk.Button(
    button_frame,
    text="",
    font=button_font,
    width=30,
    bg="#F39C12",
    fg="white",
    activebackground="#D35400",
)
button_d.grid(row=1, column=1, padx=5, pady=5)

info_frame = tk.Frame(root, bg="#2C3E50")
info_frame.pack(pady=10)

level_label = tk.Label(
    info_frame, text="Level: 1", font=label_font, bg="#2C3E50", fg="#ECF0F1"
)
level_label.grid(row=0, column=0, padx=10)

money_label = tk.Label(
    info_frame, text="Current Money: ₹0", font=label_font, bg="#2C3E50", fg="#ECF0F1"
)
money_label.grid(row=0, column=1, padx=10)

timer_label = tk.Label(
    info_frame,
    text="Time left: 30 seconds",
    font=label_font,
    bg="#2C3E50",
    fg="#ECF0F1",
)
timer_label.grid(row=0, column=2, padx=10)

lifeline_button = tk.Button(
    root,
    text="50:50 Lifeline",
    font=button_font,
    command=use_lifeline,
    bg="#9B59B6",
    fg="white",
    activebackground="#8E44AD",
)
lifeline_button.pack(pady=10)

load_question()

root.mainloop()
