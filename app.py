from tkinter import *
from turtle import bgcolor
from tkinter import ttk 

win = Tk()
win.title("Abhik Patra")
win.iconbitmap("icon.ico")
win.maxsize(width=700,height=450)
win.minsize(width=400,height=250)

# def func():
#     x=var.get()
#     print(x)

# -----------------label code
# con =StringVar()
# lbl =Label(win, text="Name")
# lbl.grid(column=0, row=0)
# lbl.pack()
# lbl.grid(row=2,column=1)
# lbl.pack()
# -----------------entryBox code

# var = StringVar()
# ent = Entry(win,width=50,font=("Arial"),textvariable=var)
# ent.place(x=80,y=10)

# chTxt = StringVar()
# lble =Label(win, text="Nothing",textvariable=chTxt)
# lble.grid(column=0, row=3)


# btn = Button(win,text="Submit",bg="green",fg="white",command=func)
# btn.place(x=80,y=80)

var = StringVar()

# com = ttk.Combobox(win,width=30)
# com['state'] = 'readonly'
# com['values'] =("Jan","Feb")
# com.current(1)
# com.place(x=10,y=10)

# def func():
#     print(chkBtn1.get())
#     print(chkBtn2.get())


# chkBtn1=IntVar()
# chkBtn2=IntVar()

# sel = Checkbutton(win,text="Male",variable=chkBtn1,onvalue=1,offvalue=0)
# sel.pack()

# sel = Checkbutton(win,text="Female",variable=chkBtn2,onvalue=1,offvalue=0)

# sel.pack()

# btn = Button(win,text="Submit",bg="green",fg="white",command=func)
# btn.place(x=80,y=80)

def func():
    print(var.get())
 

var=IntVar()

sel = Radiobutton(win,text="Male",value=0,variable=var)
sel.pack()

sel = Radiobutton(win,text="Female",value=1,variable=var)

sel.pack()
btn = Button(win,text="Submit",bg="green",fg="white",command=func)
btn.place(x=80,y=80)
win.mainloop()