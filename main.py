from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
GREY = "#808080"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 1
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    canvas.itemconfig(timer_text,text="00:00")
    checkmark_label.config(text="")
    window.after_cancel(timer)
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_min = WORK_MIN*60
    short_break_min = SHORT_BREAK_MIN *60
    long_break_min = LONG_BREAK_MIN *60
    if reps%8 == 0:
        timer_label.config(text="Break",fg=RED)
        count_down(long_break_min)
    elif reps%2==0:
        timer_label.config(text="Break",fg=PINK)
        count_down(short_break_min)
    else:
        timer_label.config(text="Timer",fg=GREEN)
        count_down(work_min)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec<10:
        count_sec = f"0{count_sec}"
    if count_min<10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        work_session = math.floor(reps/2)
        mark ="✔" * work_session
        checkmark_label.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("timeLapse")
window.config(padx=100,pady=50)
canvas= Canvas(width=200,height=224,bg =YELLOW, highlightthickness=0)
tomato_image= PhotoImage(file="tomato.png")
canvas.create_image(100,112,image = tomato_image)
timer_text = canvas.create_text(100,130,text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

checkmark_label = Label( fg=GREEN)
checkmark_label.grid(column=1,row=4)

timer_label = Label(text="Timer",fg=GREEN ,font=(FONT_NAME,40,'normal'))
timer_label.grid(column=1,row=0)

start_button = Button(text="start",command = start_timer)
start_button.grid(column=0,row=3)
stop_button = Button(text = "reset",command=reset_timer)
stop_button.grid(column=2,row=3)




window.mainloop()
