from email import message
from time import time
from tkinter import *
from tkinter import messagebox
from tracemalloc import start
from turtle import bgcolor
from tkinter import ttk 

win = Tk()

# topHeader = Frame(win)
# topHeader.pack()
# label = Label(topHeader,text="Top Part")
# label.pack()

# bottom = Frame(win)
# bottom.pack(side=BOTTOM)
# label = Label(bottom,text="Bottom Part")
# label.pack()

# def clickBtn():
#     if var.get()=="":
#         messagebox.showerror("Warnning","Empty Box")
#     else:
#         messagebox.showinfo("Your Text",var.get())
    



# var = StringVar()
# ent = Entry(win,textvariable=var)
# ent.pack()
# btn = Button(text="Click Me",command=clickBtn)
# btn.pack()
# def delFun():
#     lst.delete(ANCHOR)
# lst = Listbox(win)
# lst.pack()
# items=["Apple","Banna","Orange","Mango"] 
# for i in items:
#     lst.insert(END,i)


# btn = Button(win,text="Click To Delete",command=delFun)

# btn.pack()

# can = Canvas(win)
# cord = 10,20,87,92
# can.create_arc(cord,start=0,extent=100,fill="blue")
# can.create_line(cord)
# can.pack()



# def clsoeWin():
#     top.destroy()
# top = Toplevel()  #when open two window
# btn = Button(win,text="Close Window",command=clsoeWin).pack()
# def bar():
#     import time
#     progress['value'] = 20
#     win.update_idletasks()
#     time.sleep(1)

# progress = ttk.Progressbar(win, orient = HORIZONTAL,
#               length = 100, mode = 'determinate')
# progress.pack(pady = 10)
# btn = Button(win,text="Start",command=bar).pack()

scroll = Scrollbar(win).pack(side=RIGHT,fill=Y)

win.mainloop()