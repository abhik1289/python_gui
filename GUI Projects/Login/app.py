from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
win = Tk();


win.maxsize(width=400,height=550)
win.minsize(width=400,height=550)
win.title("Log Now")
win.iconbitmap("user.ico")
win.configure(bg='#dcdde1')

#Create a canvas
canvas= Canvas(win, width= 600, height= 400)
canvas.pack()

#Load an image in the script
img= (Image.open("login.png"))

#Resize the Image using resize method
resized_image= img.resize((300,205), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

#Add image to the Canvas Items
canvas.create_image(10,10, anchor=NW, image=new_image)

emailVal = StringVar()
pwdVal = StringVar()


def submit():
    email = emailVal.get()
    password = pwdVal.get()
    print(email)
    if (email=="" and password ==""):
        messagebox.showerror("","Fileds are empty")
    else:
        messagebox.showinfo("",f"{email+password}")


email = Label(win,text="Email",)
entryBox = Entry(win,textvariable=emailVal)
password = Label(win,text="Password")
entryBox2 = Entry(win,textvariable=pwdVal)
button = Button(win,text="Log In",command=submit)
email.pack()
entryBox.pack()
password.pack()
entryBox2.pack()
button.pack()

win.mainloop()