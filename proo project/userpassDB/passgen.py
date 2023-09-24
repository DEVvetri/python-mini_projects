from customtkinter import *
from tkinter import *
import ttkbootstrap as ttk
from PIL import ImageTk, Image

win=CTk()
win.geometry("600x700")
win._set_appearance_mode("light")

class frame1_main(CTkFrame):
    def __init__(self,master=win):
        super().__init__(master,width=500,height=600,fg_color="gray",bg_color="white")
        self.pack(pady=100)
        self.create_widgets()
    def create_widgets(self):
        self.entry_user=CTkEntry(master=self).pack(expand=True)
        self.entry_pass=CTkEntry(master=self).pack(expand=True)
frame1=frame1_main()

win.mainloop()