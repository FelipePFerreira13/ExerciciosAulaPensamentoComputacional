import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from database.database_tools import Db_Tools
from utils.Validadores import Validar

class Cadastro_Proprietarios:
    def __init__(self, master=None):
        self.root = tk.Toplevel(master) if master else tk.Tk()
        self.root.title("Cadastro de Usuário")

        tk.Label(self.root, text="Nome:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_nome = tk.Entry(self.root, width=30)
        self.entry_nome.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="CPF:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_cpf = tk.Entry(self.root, width=30)
        self.entry_cpf.grid(row=1, column=1, padx=10, pady=5)

        btn_cadastrar = tk.Button(self.root, text="Cadastrar", command=self.cadastrar_usuario)
        btn_cadastrar.grid(row=4, column=0, columnspan=2, pady=15)

    def cadastrar_usuario(self):
        nome = self.entry_nome.get()
        cpf = self.entry_cpf.get()
        if Validar.Validar_cpf(cpf):
            try:
                Db_Tools.Criar_Usuario(nome, cpf)
                messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
                self.entry_nome.delete(0, tk.END)
                self.entry_cpf.delete(0, tk.END)
            except Exception as e:
                messagebox.showerror("Erro", f"Falha ao cadastrar usuário:\n{e}")
        else:
            messagebox.showerror("Erro", "CPF inválido!")

    def show(self):
        self.root.mainloop()

# Para testar isoladamente:
if __name__ == "__main__":
    Cadastro_Proprietarios().show()