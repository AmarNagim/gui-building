from tkinter import *
from tkinter import font

# favoriete programma in tkinter

window = Tk()
window.title('Hello World')
window.geometry('250x100')

textFrame = Frame(window)
textFrame.pack(pady=28)


textLabel = Label(textFrame, text='Hello World!', font=('Arial', 20, font.BOLD)).pack()

window.mainloop()