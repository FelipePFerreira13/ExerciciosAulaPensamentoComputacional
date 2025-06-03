import tkinter as tk
from models.Proprietarios import Proprietario
from models.Carro import Carro
from models.Caminhao import Caminhao
from models.Moto import Moto
from database.database_commands import Get_Proprietarios

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