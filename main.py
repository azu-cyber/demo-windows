from tkinter import *
from datetime import date
root=Tk()
root.title('Getting Started with Wigets')
root.geometry('400x300')
lb1=Label(text="hey there!",fg="white",bg="#072F5F",height=1,
width=300)
name_lb1 = Label(text="Full Name",bg="#3895D3")
name_entry= Entry()
def display():
    name = name_entry.get
    global message
    message = "Welcome to the Application! \n Today's date is: "
    greet="Hello "+name+"\n"
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())
text_box=Text(height=3)
btn = Button(text="Begin", command=display, height=1, bg="#126140",fg="white")
lb1.pack()
name_lb1.pack()
name_entry.pack()
btn.pack()
text_box.pack()