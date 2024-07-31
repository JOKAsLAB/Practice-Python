# grid

from tkinter import *

window = Tk()

firstNameLabel = Label(window, text="First name: ").grid(row=0, column=0)
firstNameEntry = Entry(window).grid(row=0, column=1)

lastNameLabel = Label(window, text="Last name: ").grid(row=1, column=0)
lastNameEntry = Entry(window).grid(row=1, column=1)

emailNameLabel = Label(window, text="Email : ").grid(row=2, column=0)
emailNameEntry = Entry(window).grid(row=2, column=1)

window.mainloop()