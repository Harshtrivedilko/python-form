from tkinter import *

root=Tk()
root.geometry("500x500")

Label_1=Label(root,text="Username" ,font=("Italic",12),bg="black",fg="white")
Label_2=Label(root,text="Password" ,font=("Italic",12),bg="black",fg="white")

Label_1.grid(row=0)
Label_2.grid(row=1,column=0)

entry_1=Entry(root)
entry_2=Entry(root)

entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)

Button(root, text="login",fg="blue" ,bg="white",width=10).grid(row=3,column=1)

root.mainloop()
