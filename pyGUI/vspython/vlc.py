from tkinter import *
#root details
root=Tk()
root.geometry('1920x1080')
root.iconbitmap('')
#function

#button
but_play=Button(root,padx=5,pady=7)
#label
lF=LabelFrame(root,width=1920,height=700)
#position
lF.grid(row=0,column=0)
but_play.grid(row=1)
#end
root.mainloop()
