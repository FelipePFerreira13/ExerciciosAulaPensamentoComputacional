import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from screens.Cadastro_Veiculos import TelaCadastroVeiculos 
from screens.Listar_Cadastros import Listar_Cadastros 
from screens.Cadastro_Proprietarios import Cadastro_Proprietarios 
class Tela_Principal:
    
    def abrir_cadastro_veiculos(self):
        TelaCadastroVeiculos(self.janela)  # Passa a janela principal como master
        
    def abrir_cadastro_proprietario(self):
        Cadastro_Proprietarios()
        
    def abrir_listar_cadastros(self):
        Listar_Cadastros()
        
    def __init__(self):        
        self.carrega()
    def carrega(self):
        self.janela = tk.Tk()
        self.janela.title("Tela Principal")
        self.janela.geometry("800x600")
        
        
        cadastro_veiculos = tk.Button(self.janela, 
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

        cadastro_proprietario = tk.Button(self.janela, 
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
        
        listar_cadastros = tk.Button(self.janela, 
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

        
        
        
        
        
        
        
        
        
        
        
        
        self.janela.mainloop()


