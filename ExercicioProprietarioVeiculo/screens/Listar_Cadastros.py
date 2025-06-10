import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from database.database_tools import Db_Tools
class Listar_Cadastros:
    
    def __init__(self):
        
        top = tk.Tk()
        
        listbox = tk.Listbox(top, height=10, 
                             width=15, 
                             bg="grey",
                             activestyle='dotbox', 
                             font="Helvetica",
                             fg="yellow")

        top.geometry("300x250")  

        label = tk.Label(top, text="FOOD ITEMS") 

        listbox.insert(1, "Nachos")
        listbox.insert(2, "Sandwich")
        listbox.insert(3, "Burger")
        listbox.insert(4, "Pizza")
        listbox.insert(5, "Burrito")

        label.pack()
        listbox.pack()

        top.mainloop()