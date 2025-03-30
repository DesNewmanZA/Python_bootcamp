# Import needed modules
from tkinter import *
import math

# Initialize constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Initialize starting states
reps = 0
timer = None


##############
# Time reset #
##############
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text='Timer', fg=GREEN)
    check_marks.config(text='')
    canvas.itemconfig(timer_text, text='00:00')
    global reps
    reps = 0


###############
# Start timer #
###############
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        timer_label.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_MIN*60)
        timer_label.config(text='Break', fg=PINK)
    else:
        countdown(WORK_MIN*60)
        timer_label.config(text='Work', fg=GREEN)


#######################
# Countdown mechanism #
#######################
def countdown(count):
    mins = math.floor(count / 60)
    if count % 60 < 10:
        seconds = "0" + str(count % 60)
    else:
        seconds = count % 60
    time_count = f"{mins}:{seconds}"
    canvas.itemconfig(timer_text, text=time_count)

    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        for _ in range(math.floor(reps / 2)):
            check_marks.config(text='✓'*_)


############
# UI setup #
############
window = Tk()
window.title('Pomodoro timer')
window.config(padx=100, pady=50, bg=YELLOW)

# Create blank canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# Create a timer label
timer_label = Label(text="Timer", font=(FONT_NAME, 40, 'bold'), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

# Tomato image
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# Start button
start_button = Button(text="Start", bg='white', highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# Reset button
reset_button = Button(text="Reset", bg='white', highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Check marks
check_marks = Label(fg=GREEN, bg=YELLOW, font=10)
check_marks.grid(column=1, row=3)

window.mainloop()
