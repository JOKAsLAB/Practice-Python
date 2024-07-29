# open a file (file_dialog)

from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir="D:\\git hub\\Practice-Python\\course",
                                          title="Open file okay?",
                                          filetypes= (("text files", "*.txt"),
                                          ("all files", "*.*")))
    file = open(filepath, "r")
    print(file.read())
    file.close()
    

window = Tk()

button = Button(text="Open", command = openFile)
button.pack()

window.mainloop()