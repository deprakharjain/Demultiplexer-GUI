from tkinter import*
import tkinter.messagebox

win = Tk()

win.title("Demultiplexer Program")
win.geometry("600x600")
win.resizable(False, False)

ca = StringVar()
cb = StringVar()
cc = StringVar()
cd = StringVar()
ce = StringVar()
cf = StringVar()
cg = StringVar()
ch = StringVar()
ci = StringVar()


label = Label(win,text = "Demultiplexer Program",padx = 10,pady = 10,font = "Helvetica 15 bold italic",bg = "Red")
label.place(x = 120, y= 30)

label = Label(win,text = "Channel A",font = "Helvetica 10 bold ")
label.place(x = 140, y= 90)

label = Label(win,text = "Channel B",font = "Helvetica 10 bold ")
label.place(x = 140, y= 120)

label = Label(win,text = "Channel C",font = "Helvetica 10 bold ")
label.place(x = 140, y= 150)

label = Label(win,text = "Channel D",font = "Helvetica 10 bold ")
label.place(x = 140, y= 180)

label = Label(win,text = "Channel E",font = "Helvetica 10 bold ")
label.place(x = 140, y= 210)

label = Label(win,text = "Channel F",font = "Helvetica 10 bold ")
label.place(x = 140, y= 240)

label = Label(win,text = "Channel G",font = "Helvetica 10 bold ")
label.place(x = 140, y= 270)

label = Label(win,text = "Channel H",font = "Helvetica 10 bold ")
label.place(x = 140, y= 310)

label = Label(win,text = "Channel I",font = "Helvetica 10 bold ")
label.place(x = 140, y= 340)

e = Entry (win,width = 15,bd = 5,textvariable = ca)
ca.set("Sony Tv")
e.place(x = 240,y = 90)

e = Entry (win,width = 15,bd = 5,textvariable = cb)
cb.set("Sab Tv")
e.place(x = 240,y = 120)

e = Entry (win,width = 15,bd = 5,textvariable = cc)
cc.set("Star Plus")
e.place(x = 240,y = 150)

e = Entry (win,width = 15,bd = 5,textvariable = cd)
cd.set("Zee Tv")
e.place(x = 240,y = 180)

e = Entry (win,width = 15,bd = 5,textvariable = ce)
ce.set("Aaj Tak")
e.place(x = 240,y = 210)

e = Entry (win,width = 15,bd = 5,textvariable = cf)
cf.set("colors")
e.place(x = 240,y = 240)

e = Entry (win,width = 15,bd = 5,textvariable = cg)
cg.set("Hbo")
e.place(x = 240,y = 270)

e = Entry (win,width = 15,bd = 5,textvariable = ch)
ch.set("Discovery")
e.place(x = 240,y = 310)

e = Entry (win,width = 15,bd = 5,textvariable = ci)
ci.set("Life Ok")
e.place(x = 240,y = 340)

def onclick():
    tkinter.messagebox.showinfo("Selected!! Now Enjoy Watching")

button = Button(win, text = "Demultiplexer",command = onclick)
button.place(x = 240, y = 380)

label = Label(win,text = "Ctr1",font = "Helvetica 10 bold ")
label.place(x = 240, y= 420)

label = Label(win,text = "Ctrl2",font = "Helvetica 10 bold ")
label.place(x = 240, y= 450)

e = Entry (win,width = 5,bd = 5)
e.place(x = 280,y = 420)

e = Entry (win,width = 5,bd = 5)
e.place(x = 280,y = 450)



win.mainloop()
