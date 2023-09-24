from customtkinter import *
from tkinter import *
from PIL import Image,ImageTk
root=CTk()
root.geometry("400x700")
root.resizable(0,0)



def preper():
    return f'I\'m Happy to cordially invite you for joining my wedding ceremony,\n{name_boy} with {name_girl} \nand cannot begin to express how thrilled we are to share this special day with all of you...\nYour presence will make the occasion memorable and wonderful. \nPlease consider this as a personal invite and grace the occasion with your presence and wishes... \n Wedding\n{date}\n{time} \nVenu{place}\n {venu}'

#function
def action():
     
    global gen_entry,name_boy,name_girl,place,venu,date,time
    name_boy=boyname_entry.get()
    name_girl   =girlname_entry.get()
    place       =place_entry.get()
    venu        =venu_entry.get()
    date        =date_entry.get()
    time        =time_entry.get()

    gen_label=CTkLabel(master=root,text="Generated Invitation is below",font=("arial",10))
    gen_entry=CTkEntry(master=root,font=("arial",15),corner_radius=5,bg_color="transparent",height=250,width=150)
    
    gen_label.grid(row=8,column=2,pady=10,padx=(150,0))
    gen_entry.grid(row=9,column=0,columnspan=3,pady=10,padx=(150,0))
    one=preper()
    print(one)
# widgetss
frame1=CTkFrame(master=root,width=400,height=100,fg_color="white",corner_radius=15)
top_label=CTkLabel(master=root,text="WedToday",font=("arial",25))
boyname_entry   =CTkEntry(master=root,font=("arial",15),corner_radius=5,bg_color="transparent",placeholder_text="boy_name")
girlname_entry  =CTkEntry(master=root,font=("arial",15),corner_radius=5,bg_color="transparent",placeholder_text="girl_name")
place_entry     =CTkEntry(master=root,font=("arial",15),corner_radius=5,bg_color="transparent",placeholder_text="place...")
venu_entry      =CTkEntry(master=root,font=("arial",15),corner_radius=5,bg_color="transparent",placeholder_text="venu_name")
date_entry      =CTkEntry(master=root,font=("arial",15),corner_radius=5,bg_color="transparent",placeholder_text="date")
time_entry      =CTkEntry(master=root,font=("arial",15),corner_radius=5,bg_color="transparent",placeholder_text="time")

but_sub=CTkButton(master=root,text="Generate Invite",corner_radius=15,command=action)


#poss
top_label.grid(row=0,column=0,columnspan=3,padx=(150,0),pady=(5,0))
boyname_entry. grid(row=1,column=2,pady=10,padx=(150,0))
girlname_entry.grid(row=2,column=2,pady=10,padx=(150,0))
place_entry.   grid(row=3,column=2,pady=10,padx=(150,0))
venu_entry.    grid(row=4,column=2,pady=10,padx=(150,0))
date_entry.    grid(row=5,column=2,pady=10,padx=(150,0))
time_entry.    grid(row=6,column=2,pady=10,padx=(150,0))

but_sub.grid(row=7,column=2,pady=10,padx=(150,0))
root.mainloop()