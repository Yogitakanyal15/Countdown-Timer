#Countdown Timer
from tkinter import *
import time

remaining_time = 0
is_paused = False
initial_time = 0

def Start():
    global initial_time, remaining_time, is_paused
    initial_time=int(e.get())
    try:
            if initial_time>0:
                 remaining_time=initial_time
                 is_paused=False
                 countdown(remaining_time)
            else:
                 s.config(text="Value must be apositive integer!")
    except ValueError:
        s.config(text="Value must be a positive integer!")




def countdown(x): 
    global remaining_time
    if x>0:
        if not is_paused:  
         remaining_time=x; 
         min,seconds=divmod(x,60)
         hours,min=divmod(min,60)
         format=f"{hours:02d}:{min:02d}:{seconds:02d}"
         s.config(text=format)
         root.after(1000,countdown,x-1)
    else:
         s.config(text="Time is up!!")


def Pause():
     global is_paused
     is_paused=True

def Resume():
     global is_paused
     is_paused=False
     countdown(remaining_time)

def Restart():
     global initial_time
     countdown(initial_time)


root=Tk()
root.title("Countdown Timer")

entry_frame=Frame(root)
entry_frame.pack(pady=10)

l=Label(entry_frame,text="Enter the no. of seconds of timer you want: ")
l.grid(row=2,column=2,padx=10,pady=10)
e=Entry(entry_frame,width=50)
e.grid(row=2,column=5,padx=10,pady=10)

s=Label(entry_frame)
s.grid(row=3,column=4,padx=100,pady=100)

button_frame=Frame(root)
button_frame.pack(pady=10)

btn=Button(button_frame,text="Start", command=Start)
btn.grid(row=0,column=2,padx=10,pady=10)

pause=Button(button_frame,text="Pause", command=Pause)
pause.grid(row=1,column=1,padx=10,pady=10)

resume=Button(button_frame,text="Resume", command=Resume)
resume.grid(row=1,column=2,padx=10,pady=10)

restart=Button(button_frame,text="Restart", command=Restart)
restart.grid(row=1,column=3,padx=10,pady=10)



root.mainloop()