import tkinter as tk
app=tk.Tk()
class Application(tk.Frame): 
        def __init__(self, master=None):
            tk.Frame.__init__(self, master) 
            self.grid() 
            self.createWidgets()
        def createWidgets(self):
            self.quitButton = tk.Button(self, text='Quit',
            command=self.quit) 
            self.lab=tk.Label(self,text="vetri")
            self.lab.grid(row=0,column=0)
            self.quitButton.grid(row=0,column=1) 
app = Application() 
app.master.title('Sample application') 
app.mainloop()