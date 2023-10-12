from customtkinter import *
from tkinter import messagebox
import re
win=CTk()

class MAIN_FRAME(CTkFrame):
    def __init__(self):
        super().__init__(master=win,width=500,height=790)
        self.pack(anchor=W,fill=Y,expand=True)
        self.create_wid()

        
        
    def create_wid(self):
        #variables
        self.var_male=StringVar()
        self.date_get=StringVar()
        self.mon_get=StringVar()
        self.year_get=StringVar()
        self.ent_enroll=StringVar()
        self.course_st=StringVar()
        self.batch_st=StringVar()
        self.date=[]
        for i in range(1,31):
            self.date.append(str(i))
        
        self.month=["jan","feb","marh","arpl","may","jun","jul","agst","sept","oct","nov","dec"]
        self.year=[]
        for i in range(1990,2025):
            self.year.append(str(i))
         
        #labels
        self.lab1=CTkLabel(master=self,text="Student id",font=CTkFont(size=19)).grid(row=0,column=0,padx=(100,0),pady=(10,10))
        self.lab2=CTkLabel(master=self,text="Student name",font=CTkFont(size=19)).grid(row=1,column=0,padx=(100,0),pady=(10,10))
        self.lab_gen=CTkLabel(master=self,text="Student Gender",font=CTkFont(size=19)).grid(row=2,column=0,padx=(100,0),pady=(10,10))
        self.lab3=CTkLabel(master=self,text="Student Email",font=CTkFont(size=19)).grid(row=3,column=0,padx=(100,0),pady=(10,10))
        self.lab4=CTkLabel(master=self,text="Student Phone",font=CTkFont(size=19)).grid(row=4,column=0,padx=(100,0),pady=(10,10))
        self.lab5=CTkLabel(master=self,text="Student Dob",font=CTkFont(size=19)).grid(row=5,column=0,padx=(100,0),pady=(10,10))
        self.lab6=CTkLabel(master=self,text="Student address",font=CTkFont(size=19)).grid(row=6,column=0,padx=(100,0),pady=(10,10))
        self.lab7=CTkLabel(master=self,text="Student Qualification",font=CTkFont(size=19)).grid(row=7,column=0,padx=(90,0),pady=(10,10))
        self.lab8=CTkLabel(master=self,text="Student Enrollment",font=CTkFont(size=19)).grid(row=8,column=0,padx=(100,0),pady=(10,10))
        self.lab9=CTkLabel(master=self,text="Student Course",font=CTkFont(size=19)).grid(row=9,column=0,padx=(100,0),pady=(10,10))
        self.lab10=CTkLabel(master=self,text="Student Batch",font=CTkFont(size=19)).grid(row=10,column=0,padx=(100,0),pady=(10,10))
        
        
        #entry for name and reg no
        self.entry1=CTkEntry(master=self,width=300,font=CTkFont(size=19),border_color="white")
        self.entry2=CTkEntry(master=self,width=300,font=CTkFont(size=19),border_color="white")
        #checkbox for male or female
        self.entry3_1=CTkCheckBox(master=self,text="male",onvalue="male",offvalue="off",corner_radius=50,variable=self.var_male,)   
        self.entry3_2=CTkCheckBox(master=self,text="female",onvalue="female",offvalue="off",corner_radius=50,variable=self.var_male)
        #email and phone number entry box
        self.entry4=CTkEntry(master=self,width=300,font=CTkFont(size=19),border_color="white")
        self.entry5=CTkEntry(master=self,width=300,font=CTkFont(size=19),border_color="white")
        #birth drop
        self.date_drop=CTkOptionMenu(master=self,width=50,fg_color="gray",button_color="black",values=self.date,variable=self.date_get)
        self.mon_drop=CTkOptionMenu(master=self,width=70,fg_color="gray",button_color="black",values=self.month,variable=self.mon_get) 
        self.yer_drop=CTkOptionMenu(master=self,width=70,fg_color="gray",button_color="black",values=self.year,variable=self.year_get)
        self.date_drop.set("date")
        self.mon_drop .set("month")
        self.yer_drop .set("year")
        #address and qualification entry box
        self.entry7=CTkEntry(master=self,width=300,font=CTkFont(size=19),border_color="white")
        self.entry8=CTkEntry(master=self,width=300,font=CTkFont(size=19),border_color="white")
        #enrollment menu
        self.entry9=CTkOptionMenu(master=self,width=120,fg_color="gray",button_color="black",values=["management","counseling"],variable=self.ent_enroll)
        self.entry9.set("Enrollment")
        #course menu 
        self.course_drop=CTkOptionMenu(master=self,width=90,fg_color="gray",button_color="black",values=["CSE","IT","EEE","MECH","OTHER"],variable=self.course_st)
        self.course_drop.set("course")
        #batch menu
        self.batch_drop=CTkOptionMenu(master=self,width=90,fg_color="gray",button_color="black",values=["2020","2021","2022","2023","2024","2025"],variable=self.batch_st)
        self.batch_drop.set("batch")
        #submit button-------------------------------------------
        self.but=CTkButton(master=self,text="Submit",width=150,height=30,fg_color="black",hover_color="gray",hover=True,font=CTkFont(size=19),command=self.but_action_check_id)



        #position--------------------------------------------
            #entry for name and reg no
        self.entry1.grid(row=0,column=1,padx=(5,100),pady=(10,10),columnspan=1)
        self.entry2.grid(row=1,column=1,padx=(5,100),pady=(10,10),columnspan=1)
            #checkbox for male or female
        self.entry3_1.grid(row=2,padx=(50,0),pady=(10,10),columnspan=2)
        self.entry3_2.grid(row=2,padx=(220+50,0),pady=(10,10),columnspan=2)
            #email and phone number entry box
        self.entry4.grid(row=3,column=1,padx=(5,100),pady=(10,10),columnspan=1)
        self.entry5.grid(row=4,column=1,padx=(5,100),pady=(10,10),columnspan=1)
            #birth drop
        self.date_drop.grid(row=5,padx=(0,0),pady=(10,10),columnspan=2)
        self.mon_drop.grid(row=5,padx=(210,0),pady=(10,10),columnspan=2)
        self.yer_drop.grid(row=5,padx=(425,0),pady=(10,10),columnspan=2)
            #address and qualification entry box
        self.entry7.grid(row=6,column=1,padx=(5,100),pady=(10,10))
        self.entry8.grid(row=7,column=1,padx=(5,100),pady=(10,10))
            #enrollment menu
        self.entry9.grid(row=8,column=1,padx=(5,100),pady=(10,10))
            #course menu 
        self.course_drop.grid(row=9,column=1,padx=(5,100),pady=(10,10))
        #submit button
        self.batch_drop.grid(row=10,column=1,padx=(5,100),pady=(10,10))

        self.but.grid(row=11,columnspan=2,padx=(50,100),pady=(10,10))
#checking reg no
    def but_action_check_id(self):
        self.reg_no=self.entry1.get()
        if self.reg_no.isnumeric()==True:
            self.but_action_check_name()
        else:
            messagebox.showerror("error","plz check id of std")
#checking name
    def but_action_check_name(self):
        self.std_name=self.entry2.get()
        if self.std_name.isalpha()==True:
            self.but_action_check_gender()
        else:
            messagebox.showerror("error","plz check name of std")
#checking gender 
    def but_action_check_gender(self):
        self.num_male=self.var_male.get()
        if self.num_male=="male" or self.num_male=="female":
            self.but_action_check_email()
        else:
            messagebox.showinfo("note","plz check gender of std")
#checking email    
    def but_action_check_email(self):
        self.mail=self.entry4.get()
        self.pattren=re.compile(r'([a-z0-9]+[.-_])*[a-z0-9]+@[a-z]')
        if re.search(self.pattren,self.mail):
            self.but_action_check_phone()
        else:
            messagebox.showinfo("note","plz check email of std")
#checking ph  no
    def but_action_check_phone(self):
        self.std_number=self.entry5.get()
        if self.std_number.isnumeric():
            
            self.but_action_check_dob()
        else:
            messagebox.showinfo("note","plz check phone no of std")
#checking DOB
    def but_action_check_dob(self):
        self.date_DD=self.date_get.get()
        
        self.date_MM=self.mon_get.get()
        
        self.date_yy=self.year_get.get()
        
        if self.date_DD=="date" or self.date_MM=="month" or self.date_yy=="year":
            messagebox.showinfo("note","plz check date of birth of std")
        else:
            self.DOB=f'{self.date_DD}:{self.date_MM}:{self.date_yy}'
            self.but_action_check_add()
#checking address
    def but_action_check_add(self):
        self.std_address=self.entry7.get()
        self.but_action_check_qualifiction()
#checking qualifiction
    def but_action_check_qualifiction(self):
        self.qualifiction_std=self.entry8.get()
        self.but_action_check_enroll()
#checking enrollment
    def but_action_check_enroll(self):
        self.enroll_status=self.ent_enroll.get()
        if self.enroll_status=="Enrollment":
            messagebox.showinfo("note","plz check enrollment of std")
        else:
            self.but_action_check_course()
            
#checking course
    def but_action_check_course(self):
        self.course_of_st=self.course_st.get()
        if self.course_of_st=="course":
            messagebox.showinfo("note","plz check course of std")
        else:
            self.but_action_check_batch()
            
#checking batch
    def but_action_check_batch(self):
        self.batch_of_st=self.batch_st.get()
        if self.batch_of_st=="batch":
            messagebox.showinfo("note","plz check batch of std")
        else:
            messagebox.showinfo("success","your details are submited")
            self.data_proessing()
    def data_proessing(self):
        print(self.reg_no)
        print(self.std_name)
        print(self.num_male)
        print(self.mail)
        print(self.std_number)
        print(self.DOB)
        print(self.std_address)
        print(self.qualifiction_std)
        print(self.enroll_status)
        print(self.course_of_st)
        print(self.batch_of_st)
        self.entry1.delete(0,END)
        self.entry2.delete(0,END)
        self.entry4.delete(0,END)
        self.entry5.delete(0,END)
        self.entry7.delete(0,END)
        self.entry8.delete(0,END)

        self.entry3_1.deselect("off")
        self.entry3_2.deselect("off")

        self.date_drop.set("date")
        self.mon_drop.set("month")
        self.yer_drop.set("year")


        self.entry9.set("Enrollment")
        self.course_drop.set("course")
        self.batch_drop.set("batch")

main=MAIN_FRAME()
win.mainloop()