# buttons

from tkinter import *

count = 0
def click():
    global count
    count += 1
    print(count)

window = Tk()

photo = PhotoImage(file="course\\66.jokas_lab.png")

button = Button(window,
                text="click me!",
                command= click,
                font=("Comic Sans", 25),
                fg="green",
                bg="black",
                activeforeground="green",
                activebackground="black",
                state=ACTIVE,
                image = photo,
                compound= "top")


button.pack()

window.mainloop()