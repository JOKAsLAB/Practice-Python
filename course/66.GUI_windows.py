# GUI windows

from tkinter import *

window = Tk()

window.geometry("420x420")
window.title("Joca Martins Teste App Python")

icon = PhotoImage(file="course\\66.jokas_lab.png")
window.iconphoto(True, icon)

window.config(back="#b1d6e3")

window.mainloop()