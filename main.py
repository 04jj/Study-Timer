from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
PURPLE = "#af8bf7"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
times = 0

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    title_label.config(text = "Timer")
    check_marks.config(text = "")
    global times
    times = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global times
    times += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if times % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text = "BREAK", fg = RED)
    elif times % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text = "BREAK", fg = PURPLE)
    else:
        count_down(work_sec)
        title_label.config(text = "STUDY", fg = GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(times/2)
        for _ in work_sessions:
            marks += "✓"
        check_marks.config(text = marks) 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)

title_label = Label(text = "Timer", fg = PINK, bg = YELLOW, font = (FONT_NAME, 40))
title_label.grid(column = 1, row = 0)

canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
cupcake_img = PhotoImage(file = "cupcakie.png")
canvas.create_image(100, 112, image = cupcake_img)
timer_text = canvas.create_text(100, 160, text = "00:00", fill = "white", font = (FONT_NAME, 25, "bold"))
canvas.grid(column = 1, row = 1)

start_button = Button(text = "Start", highlightthickness = 0, command = start_timer)
start_button.grid(column = 0, row = 2)

reset_button = Button(text = "Reset", highlightthickness = 0, command = timer_reset)
reset_button.grid(column = 2, row = 2)

check_marks = Label(fg = PINK, bg = YELLOW, font = (FONT_NAME, 12, "bold"))
check_marks.grid(column = 1, row = 3)


window.mainloop()
