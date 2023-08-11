from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
r=Tk()
def openfil():
    
    global s_image
    r.file=filedialog.askopenfilename(initialdir="D:/coding learn/pyGUI/vspython",title="select",filetypes=(("python files","*.py"),("all files","*.*")))
    s_image=ImageTk.PhotoImage(Image.open(r.file))
    lab=Label(r,image=s_image)
    lab.pack()
but=Button(r,text="open",command=openfil)
but.pack()
r.mainloop()