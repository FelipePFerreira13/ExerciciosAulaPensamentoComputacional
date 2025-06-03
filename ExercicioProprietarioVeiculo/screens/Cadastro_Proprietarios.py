import tkinter as tk
from models.Proprietarios import Proprietario

class Cadastro_Proprietario:
    

    def __init__(self):        

        janela = tk.Tk()
        janela.title("Cadastro de Proprietário")
        janela.geometry("800x600")
        nome = tk.Entry(janela)
        nome.grid(row=2,column=4,pady=2)
        cpf = tk.Entry(janela)
        cpf.grid(row=3,column=4,pady=2)
        
        fazer_cadastro = tk.Button(janela, 
                        text="Cadastrar Proprietário", 
                        command=self.fazer_cadastro,
                        activebackground="blue", 
                        activeforeground="white",
                        anchor="center",
                        bd=3,
                        bg="lightgray",
                        cursor="hand2",
                        disabledforeground="gray",
                        fg="black",
                        font=("Arial", 12),
                        height=2,
                        highlightbackground="black",
                        highlightcolor="green",
                        highlightthickness=2,
                        justify="center",
                        overrelief="raised",
                        padx=10,
                        pady=5,
                        width=15,
                        wraplength=100)
        
        
        
        
        
        
        
        
        
        
        
        janela.mainloop()
        
        

            
            
    def fazer_cadastro(event):
        nome = nome.get()
        cpf = cpf.get()
        
        proprietario = Proprietario(nome, cpf)
        return value
