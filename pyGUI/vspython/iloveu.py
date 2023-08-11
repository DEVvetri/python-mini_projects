from tkinter import *

root=Tk()
root.geometry('1920x1080')
my_can=Canvas(root,width=1000,height=1000,bg="pink")
my_can.pack(pady=25)
#I letter start
my_can.create_line((100,50,300,50),fill="black")

my_can.create_line((100,50,100,100),fill="black")
my_can.create_line((300,50,300,100),fill="black")

my_can.create_line((100,100,150,100),fill="black")
my_can.create_line((250,100,300,100),fill="black")

my_can.create_line((150,400,150,100),fill="black")
my_can.create_line((250,400,250,100),fill="black")

my_can.create_line((100,400,100,450),fill="black")
my_can.create_line((300,400,300,450),fill="black")

my_can.create_line((100,400,150,400),fill="black")
my_can.create_line((250,400,300,400),fill="black")

my_can.create_line((100,450,300,450),fill="black")
#I letter END
#heart draw start
my_can.create_arc(360,50,520,250,start=0,extent=180,fill="red",outline="red")
my_can.create_arc(520,50,680,250,start=0,extent=180,fill="red",outline="red")

my_can.create_polygon(359,150,678,150,520,450,fill="red")
#heart draw END

#u letter START
my_can.create_line(750,50,800,50)
my_can.create_line(900,50,950,50)

my_can.create_line(750,50,750,450)
my_can.create_line(950,50,950,450)

my_can.create_line(800,50,800,400)
my_can.create_line(900,50,900,400)
my_can.create_line(800,400,900,400)

my_can.create_line(750,450,950,450)
#u letter END
root.mainloop()