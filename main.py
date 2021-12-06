# import modules
from tkinter import *
import calendar
# create a tkinter window
root = Tk()
root.title("Calendar")
root.geometry("350x250")
root.configure(bg='#B21368')
root.resizable(0, 0)


# defining a function to display calendar
def show():
    m = int(spin1.get())
    y = int(spin2.get())
    cal = calendar.month(y, m)
    txt.delete(0.0, END)
    txt.insert(INSERT, cal)

# creating labels for month and year


l1 = Label(root, text="Month", bg='#D67BA8', fg='#0A0708', font=('arial', 12, 'bold')).place(x=40, y=10)
l2 = Label(root, text="Year", fg='#0A0708', bg='#D67BA8', font=('arial', 12, 'bold')).place(x=220, y=10)

# creating spinbox
spin1 = Spinbox(root, bg='#D67BA8', values=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12), width=4)
spin1.place(x=100, y=10)
spin2 = Spinbox(root, bg='#D67BA8', from_=1969, to=2200, width=4)
spin2.place(x=270, y=10)

# creating button
btn = Button(root, text="Show", font=('arial', 12, 'bold'), bg='#D67BA8', command=show).place(x=145, y=40)

# creating textbox to display calendar
txt = Text(root, fg='#0A0708', width=22, height=8)
txt.place(x=80, y=87)
root.mainloop()