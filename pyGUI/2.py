from tkinter import *
def my_frist():
    l=Label(r,text="vanag bro play panalam ma")
    but=Button(r,text="PLAY",border=6)
    l.pack()
    but.pack()
r = Tk()
r.title('Counting Seconds')
r.geometry("350x550")
button =Button(r, text='LET\'S START', width=15, command=my_frist)
button.pack()
r.mainloop()
