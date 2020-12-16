# Icon attribution: Freepik
from tkinter import *
from datetime import datetime

root = Tk()
root.geometry("250x300")
root.title("Stopwatch")
icon = PhotoImage(file = "stopwatch.png")
root.iconphoto(False, icon)

global time
time = 0

global flag
flag = 0

def getTime(): # Setting the time and displaying it
    global flag
    if flag == 0: # if flag is zero, time will be updated
        reset_button.config(state = DISABLED)
        global time
        time  += 1
        hrs = time//3600
        mins = (time%3600)//60
        secs = (time%3600)%60
        string = f"{hrs}:{mins}:{secs}"
        label.config(text = datetime.strptime(string, '%H:%M:%S').time())
        label.after(1000, getTime) # After every 1000 milliseconds (1 sec), call the getTime function

def stopTime():
    global time
    global flag
    flag = 1 # flag is made 1 to indicate that the stopwatch has to stop running / updating
    reset_button.config(state = NORMAL)
    start_button.config(state = DISABLED)

def resetTime():
    global time
    global flag
    time = 0 # time is reset to zero
    label.config(text = "00:00:00")
    flag = 0
    start_button.config(state = NORMAL)

# Initial setup of the stopwatch
label = Label(root, text = "00:00:00", font = "Arial 20 bold", pady = 20)
label.pack()

start_button = Button(root, text = "Start", font = "Arial 16", padx = 10, pady = 10, command = getTime)
start_button.pack()

stop_button = Button(root, text = "Stop", font = "Arial 16", padx = 10, pady = 10, command = stopTime)
stop_button.pack()

reset_button = Button(root, text = "Reset", font = "Arial 16", padx = 15, pady = 10, command = resetTime)
reset_button.pack()

root.mainloop()
