from tkinter import *
from datetime import datetime
import sqlite3
from tkinter import messagebox
#details of window
log=Tk()
log.geometry("1920x1080")
log.title("ksrct lab log DB")
my_can=Canvas(log,width=1920,height=1080,bg="white")
my_can.place(x=0,y=0)
#database set
#connect to database
data=sqlite3.connect("studentlog.db")
c=data.cursor()

#create databasse
# c.execute("""CREATE TABLE studentlog(
#             STUDENT_NAME text,
#             STUDENT_REG_NO integer,
#             STUDENT_ROLL_NO integer,
#             STUDENT_DEGREE text,
#             STUDENT_SECTION text,
#             YEAR text
# )""")
#function
def submit_recod():
    name=name_of_student_entry.get()
    roll=student_rollno_entry.get()
    regno=student_regno_entry.get()
    degree=name_of_degree_entry.get()
    section=name_of_section_entry.get()
    year=student_year_entry.get()
    if name=='' and roll=='' and regno=='' and degree=='' and section=='' and year=='':
        messagebox.showwarning("error","Don't leave any data empty")
    else:
        data=sqlite3.connect("studentlog.db")
        c=data.cursor()

        c.execute("INSERT INTO studentlog VALUES(:STUDENT_NAME,:STUDENT_REG_NO,:STUDENT_ROLL_NO,:STUDENT_DEGREE,:STUDENT_SECTION,:YEAR)",
                {
                    'STUDENT_NAME': name_of_student_entry.get(),
                    'STUDENT_REG_NO': student_regno_entry.get(),
                    'STUDENT_ROLL_NO': student_rollno_entry.get(),
                    'STUDENT_DEGREE' :name_of_degree_entry.get(),
                    'STUDENT_SECTION' :name_of_section_entry.get(),
                    'YEAR':student_year_entry.get()
                }
                )
        c.execute("SELECT * FROM studentlog")
        datas=c.fetchall()
        print(datas)
        data.commit()
        data.close()
        name_of_student_entry.delete(0,END)
        student_regno_entry.delete(0,END)
        student_rollno_entry.delete(0,END)
        name_of_degree_entry.delete(0,END)
        name_of_section_entry.delete(0,END)
        student_year_entry.delete(0,END)
        complet=Label(log,text="successfully submited ",font=('arial',15)).place(x=700,y=570)
        for i in datas:
            success=Label(log,text=i,font=('arial',15),bg="white").place(x=750,y=600)
#labels
name_of_student=Label(log,text="STUDENT_NAME",font=('arial',15),bg="white")
student_regno=Label(log,text="STUDENT_REG_NO",font=('arial',15),bg="white")
student_rollno=Label(log,text="STUDENT_ROLL_NO",font=('arial',15),bg="white")
name_of_degree=Label(log,text="STUDENT_DEGREE",font=('arial',15),bg="white")
name_of_section=Label(log,text="STUDENT_SECTION",font=('arial',15),bg="white")
student_year=Label(log,text="(I,II,III,IV) YEAR",font=('arial',15),bg="white")



my_can.create_line(750,200,750,480)
#entry
name_of_student_entry=Entry(log,width=20,font=('arial',15),bd=3)
student_regno_entry=Entry(log,width=20,font=('arial',15),bd=3)
student_rollno_entry=Entry(log,width=20,font=('arial',15),bd=3)
name_of_degree_entry=Entry(log,width=20,font=('arial',15),bd=3)
name_of_section_entry=Entry(log,width=20,font=('arial',15),bd=3)
student_year_entry=Entry(log,width=20,font=('arial',15),bd=3)

#button
submit_button=Button(log,text="SUBMIT",padx=10,pady=5,command=submit_recod).place(x=800,y=500)
#position
#lables_position
name_of_student.place(x=585,y=200)
student_regno.place(x=560,y=250)
student_rollno.place(x=550,y=300)
name_of_degree.place(x=555,y=350)
name_of_section.place(x=550,y=400)
student_year.place(x=590,y=450)
#entry position
name_of_student_entry.place(x=760,y=200)
student_regno_entry.place(x=760,y=250)
student_rollno_entry.place(x=760,y=300)
name_of_degree_entry.place(x=760,y=350)
name_of_section_entry.place(x=760,y=400)
student_year_entry.place(x=760,y=450)

#database save
data.commit()
#database close
data.close()
#END of window
log.mainloop()