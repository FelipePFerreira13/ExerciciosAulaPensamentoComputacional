import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from database.database_tools import Db_Tools

BG_COLOR = "#f0f4f8"
FONT = ("Segoe UI", 12)

# Crio a janela principal da tela de apartamentos
root = tk.Tk()
root.title("Lista de Apartamentos")
root.configure(bg=BG_COLOR)
root.state('zoomed')
root.resizable(True, True)

# Frame central onde vai a tabela
content_frame = tk.Frame(root, bg=BG_COLOR)
content_frame.pack(expand=True, fill="both")

# Função que monta e exibe a tabela de apartamentos
def listar_apartamentos():
    # Limpo widgets antigos antes de desenhar a tabela de novo
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Título da tela
    tk.Label(content_frame, text="Apartamentos Cadastrados", bg=BG_COLOR, font=("Segoe UI", 20, "bold")).pack(pady=(0, 10))

    # Crio a tabela (Treeview) com as colunas que quero mostrar
    tree = ttk.Treeview(
        content_frame,
        columns=("ID", "Número", "Valor", "ID Prédio", "Rua", "Número Prédio", "Bairro", "Cidade", "Estado"),
        show="headings",
        height=25
    )
    tree.pack(expand=True, fill="both", padx=10, pady=10)

    # Defino os nomes das colunas na tabela
    tree.heading("ID", text="ID")
    tree.heading("Número", text="Nº Ap.")
    tree.heading("Valor", text="Valor")
    tree.heading("ID Prédio", text="ID Prédio")
    tree.heading("Rua", text="Rua")
    tree.heading("Número Prédio", text="Nº Prédio")
    tree.heading("Bairro", text="Bairro")
    tree.heading("Cidade", text="Cidade")
    tree.heading("Estado", text="UF")

    # Defino larguras e alinhamento das colunas para caber tudo certinho
    tree.column("ID", width=60, anchor="center")
    tree.column("Número", width=80, anchor="center")
    tree.column("Valor", width=90, anchor="center")
    tree.column("ID Prédio", width=80, anchor="center")
    tree.column("Rua", width=180, anchor="center")
    tree.column("Número Prédio", width=90, anchor="center")
    tree.column("Bairro", width=120, anchor="center")
    tree.column("Cidade", width=120, anchor="center")
    tree.column("Estado", width=60, anchor="center")

    # Pego todos os apartamentos do banco para mostrar na tabela
    apartamentos = Db_Tools.Puxar_Apartamentos()
    for a in apartamentos:
        predio = a.predio  # Relacionamento: pego o prédio desse apartamento
        # Insiro uma linha na tabela com os dados do apartamento e do prédio
        tree.insert(
            "",
            "end",
            values=(
                a.id,
                a.numero_apartamento,
                a.valor,
                predio.id if predio else "",
                predio.rua if predio else "",
                predio.numero if predio else "",
                predio.bairro if predio else "",
                predio.cidade if predio else "",
                predio.estado if predio else ""
            )
        )

    # Função chamada quando clico no botão de comprar apartamento
    def on_comprar():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("Aviso", "Selecione um apartamento para comprar.")
            return
        item = tree.item(selected[0])
        apartamento_id = item["values"][0]
        comprar_apartamento(apartamento_id)

    # Botão para comprar o apartamento selecionado
    btn_comprar = tk.Button(content_frame, text="Comprar Apartamento Selecionado", command=on_comprar, bg="#43aa8b", fg="#fff", font=FONT)
    btn_comprar.pack(pady=10)

# Função que abre a janela para digitar o CPF e confirmar a compra
def comprar_apartamento(apartamento_id):
    compra_win = tk.Toplevel(root)
    compra_win.title("Comprar Apartamento")
    compra_win.geometry("350x180")
    compra_win.resizable(False, False)
    tk.Label(compra_win, text=f"Comprar Apartamento ID {apartamento_id}", font=("Segoe UI", 14, "bold")).pack(pady=10)
    tk.Label(compra_win, text="Digite o CPF do comprador:", font=FONT).pack(pady=5)
    entry_cpf = tk.Entry(compra_win, font=FONT)
    entry_cpf.pack(pady=5)

    # Função chamada ao clicar em confirmar compra
    def confirmar_compra():
        cpf = entry_cpf.get().strip()
        if not cpf:
            messagebox.showerror("Erro", "Digite um CPF válido.")
            return
        try:
            resultado = Db_Tools.Comprar_Apartamento(apartamento_id, cpf)
            if resultado and isinstance(resultado, int):
                messagebox.showinfo("Sucesso", f"Compra registrada com sucesso!\nSemana alugada: {resultado}")
                compra_win.destroy()
            else:
                messagebox.showerror("Erro", "Falha ao registrar compra. Verifique o CPF ou apartamento.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao registrar compra:\n{e}")

    tk.Button(compra_win, text="Confirmar Compra", command=confirmar_compra, bg="#4a90e2", fg="#fff", font=FONT).pack(pady=15)

# Mostro a tabela de apartamentos ao abrir a tela
listar_apartamentos()
root.mainloop()