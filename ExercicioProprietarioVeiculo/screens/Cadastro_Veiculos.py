import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import ttk, messagebox
from database.database_tools import Db_Tools
from utils.Validadores import Validar

class TelaCadastroVeiculos:
    def __init__(self, master=None):
        self.root = tk.Toplevel(master) if master else tk.Tk()
        self.root.title("Cadastro de Veículos")
        self.root.geometry("500x350")
        self._montar_tela()

    def get_usuarios(self):
        try:
            return Db_Tools.Listar_Usuarios()
        except Exception:
            return []

    def cadastrar_veiculo(self, tipo, entries, proprietario_var):
        placa = entries['placa'].get()
        marca = entries['marca'].get()
        modelo = entries['modelo'].get()
        ano = entries['ano'].get()
        proprietario_id = proprietario_var.get()
        if not proprietario_id:
            messagebox.showerror("Erro", "Selecione um proprietário!")
            return
        try:
            if tipo == "carro":
                Db_Tools.Criar_Carro(placa, marca, modelo, ano, tipo, proprietario_id)
            
            elif tipo =="caminhao":
                Db_Tools.Criar_Caminhao(placa, marca, modelo, ano, tipo, proprietario_id)
            
            elif tipo =="moto":
                Db_Tools.Criar_Moto(placa, marca, modelo, ano, tipo, proprietario_id)
            messagebox.showinfo("Sucesso", f"{tipo.capitalize()} cadastrado com sucesso!")
            for entry in entries.values():
                entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao cadastrar veículo:\n{e}")

    def _montar_tela(self):
        # Frame lateral para proprietários
        frame_prop = tk.Frame(self.root)
        frame_prop.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        tk.Label(frame_prop, text="Selecione o Proprietário:", font=("Arial", 10, "bold")).pack(anchor="w")

        usuarios = self.get_usuarios()
        self.proprietario_var = tk.StringVar()
        for uid, nome in usuarios:
            print(f'{uid}, {nome}')
            tk.Radiobutton(frame_prop, text=nome, variable=self.proprietario_var, value=str(uid)).pack(anchor="w")

        # Frame principal com abas
        frame_main = tk.Frame(self.root)
        frame_main.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        notebook = ttk.Notebook(frame_main)
        notebook.pack(fill=tk.BOTH, expand=True)

        def criar_aba(tipo):
            aba = tk.Frame(notebook)
            entries = {}
            labels = [("Placa", "placa"), ("Marca", "marca"), ("Modelo", "modelo"), ("Ano", "ano")]
            for i, (label, key) in enumerate(labels):
                tk.Label(aba, text=label + ":").grid(row=i, column=0, padx=10, pady=5, sticky="e")
                entry = tk.Entry(aba, width=30)
                entry.grid(row=i, column=1, padx=10, pady=5)
                entries[key] = entry
            btn = tk.Button(
                aba,
                text=f"Cadastrar {tipo.capitalize()}",
                command=lambda: self.cadastrar_veiculo(tipo, entries, self.proprietario_var)
            )
            btn.grid(row=len(labels), column=0, columnspan=2, pady=15)
            return aba

        notebook.add(criar_aba("carro"), text="Carro")
        notebook.add(criar_aba("caminhao"), text="Caminhão")
        notebook.add(criar_aba("moto"), text="Moto")

    def show(self):
        self.root.mainloop()

# Para testar isoladamente:
if __name__ == "__main__":
    TelaCadastroVeiculos().show()