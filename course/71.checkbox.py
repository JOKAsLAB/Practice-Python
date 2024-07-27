# checkbox

from tkinter import *

def display():
    if(x.get()==1):
        print("You agree!")
    else:
        print("You don't agree :(")

window = Tk()
python_photo = PhotoImage(file="course\\66.jokas_lab.png")

x = IntVar()

check_button = Checkbutton(window, 
                           text="I agree to something",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=("Arial", 20),
                           fg="green",
                           bg="black",
                           activeforeground="green",
                           activebackground="black",
                           padx=25,
                           pady=10,
                           image=python_photo,
                           compound="left")

check_button.pack()
window.mainloop()