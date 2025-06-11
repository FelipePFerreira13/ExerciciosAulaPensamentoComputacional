import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from database.database_tools import Db_Tools

class Listar_Cadastros:
    def __init__(self):
        top = tk.Tk()
        top.title("Veículos Cadastrados")
        top.geometry("700x400")

        label = tk.Label(top, text="Veículos cadastrados:")
        label.pack()

        listbox = tk.Listbox(top, height=20, width=100, bg="white", font="Helvetica", fg="black")
        listbox.pack(pady=10)

        veiculos = Db_Tools.Listar_Veiculos()
        if veiculos:
            for v in veiculos:
                # Espera-se que v seja uma tupla: (placa, modelo, ano, marca, proprietario)
                listbox.insert(
                    tk.END,
                    f"Placa: {v[0]} | Modelo: {v[1]} | Ano: {v[2]} | Marca: {v[3]} | Proprietário: {v[4]}"
                )
        else:
            listbox.insert(tk.END, "Nenhum veículo cadastrado.")

        top.mainloop()