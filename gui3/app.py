from tkinter import *


root = Tk()

my_menu = Menu(root);
root.config(menu=my_menu)
file_menu  = Menu(my_menu)
my_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_cascade(label="New")
file_menu.add_cascade(label="Open")


edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_cascade(label="Cut")
edit_menu.add_separator()
edit_menu.add_cascade(label="Copy")




root.mainloop()

