import sqlite3
from customtkinter import *
data=sqlite3.connect('studentlog.db')

c=data.cursor()

data.commit()

data.close()