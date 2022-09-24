from tkinter import *
root = Tk()
#Title
f1 = Frame(root, bg = "green",bd=25)
f1.pack()
f1.place(x=125,y=150)
l =Label(f1, text ="Hi! Wellcome to my new project.",bg = "light green",fg="red",font = "true 10",relief=RAISED)
l.pack()
#Login page
#username
Text = Label(text = "User",padx=50,pady = 10,relief = "groove",bg = "white",fg ="red",font="true 8 bold")
Text.pack(anchor="w")
Text.place(y=300)
T = Entry(bg = "cyan",font="true 10 bold")
T.pack()
T.place(x=200,y=300)
#password
Passwd = Label(text = "Password",padx=0,pady = 10,relief = "groove",bg = "white",fg = "red",font="true 8 bold")
Passwd.pack()
Passwd.place(x=0,y=450)
P = Entry(bg = "cyan",font="true 10 bold")
P.pack()
P.place(x=200,y=450)
#login button
B = Button(text = "Login",bg = "blue")
B.pack(side = TOP,fill=Y)
B.place(x=420,y=600)
root.mainloop()
