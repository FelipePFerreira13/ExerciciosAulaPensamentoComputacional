import tkinter as tk
from .Cadastro_Veiculos import Cadastro_Veiculos 
from .Listar_Cadastros import Listar_Cadastros 
from .Cadastro_Proprietarios import Cadastro_Proprietario 
from .Status_Tela import Status_Tela 
class Tela_Principal:
    
    
    def mostrar_opcao():
        rotulo.config(text=f"Escolheu: {opcao.get()}")
    
    def abrir_cadastro_veiculos(self):
        Cadastro_Veiculos()
        
    def abrir_cadastro_proprietario(self):
        Cadastro_Proprietario()
        
    def abrir_listar_cadastros(self):
        Listar_Cadastros()
        
    def __init__(self):        
        self.carrega()
        status = Status_Tela()
    def carrega(self):
        janela = tk.Tk()
        def button_clicked():
            print("Button clicked!")
        janela.title("Tela Principal")
        janela.geometry("800x600")
        
        # Creating a button with specified options
        cadastro_veiculos = tk.Button(janela, 
                        text="Cadastrar Veículo", 
                        command=self.abrir_cadastro_veiculos,
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

        cadastro_proprietario = tk.Button(janela, 
                        text="Cadastrar Proprietário", 
                        command=self.abrir_cadastro_proprietario,
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
        
        listar_cadastros = tk.Button(janela, 
                        text="Listar Cadastros", 
                        command=self.abrir_listar_cadastros,
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

        cadastro_veiculos.pack(padx=20, pady=20)
        cadastro_proprietario.pack(padx=20, pady=20)
        listar_cadastros.pack(padx=20, pady=20)

        
        
        
        
        
        
        
        
        
        
        
        
        janela.mainloop()
        
        
    def get_entry_value(event):
        value = entrada.get()
        return value
