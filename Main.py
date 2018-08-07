from tkinter import *

main = Tk()
main.title('CLICK ME')
main.geometry('300x300')
main.resizable(width=FALSE, height=FALSE)

name = StringVar()

def print_name():
    name.set('Hammad Ahmed')

def clear_name():
    name.set('')

btn = Button(main, text='Click Me!', command=lambda : print_name())
btn.place(x=120, y=2)

btn2 = Button(main, text='Clear', command=lambda : clear_name())
btn2.place(x=130, y=30)

label = Label(main, textvariable=name)
label.place(x=100, y=150)


main.mainloop()