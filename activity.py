from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.geometry('300x300')

greeting = Label(text="Hello", fg='black', bg='white')

button = Button(text='click me', bg='black', fg='white')

entry = Entry(fg='yellow', bg='blue', width=50)

greeting.pack()
button.pack()
entry.pack()

frame = Frame(master=window, relief=RAISED, borderwidth=5)
frame.pack()
label = Label(master=frame, text='sample Frame')
label.pack()

Textbox = Text(fg='green', bg='yellow')
Textbox.pack()