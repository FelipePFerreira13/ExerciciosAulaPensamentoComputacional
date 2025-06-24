import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from database.database_tools import Db_Tools

# Padrão visual igual à tela principal
BG_COLOR = "#e9eef6"
CARD_COLOR = "#ffffff"
BTN_BG = "#223a5e"
BTN_FG = "#fffbe7"
BTN_HOVER = "#e9b949"
TITLE_COLOR = "#223a5e"
DESC_COLOR = "#4a5568"
FONT_TITLE = ("Segoe UI", 28, "bold")
FONT_DESC = ("Segoe UI", 13, "italic")
FONT_BTN = ("Segoe UI", 15, "bold")
FONT = ("Segoe UI", 14)

root = tk.Tk()
root.title("Lista de Apartamentos")
root.configure(bg=BG_COLOR)
root.state('zoomed')
root.resizable(True, True)

def on_enter(e):
    e.widget['background'] = BTN_HOVER
    e.widget['fg'] = "#223a5e"

def on_leave(e):
    e.widget['background'] = BTN_BG
    e.widget['fg'] = BTN_FG

content_frame = tk.Frame(root, bg=BG_COLOR)
content_frame.pack(expand=True, fill="both")

def listar_apartamentos():
    for widget in content_frame.winfo_children():
        widget.destroy()

    tk.Label(
        content_frame, text="Apartamentos Cadastrados",
        bg=BG_COLOR, fg=TITLE_COLOR, font=FONT_TITLE
    ).pack(pady=(0, 10))

    tree = ttk.Treeview(
        content_frame,
        columns=("ID", "Número", "Valor", "ID Prédio", "Rua", "Número Prédio", "Bairro", "Cidade", "Estado"),
        show="headings",
        height=25
    )
    tree.pack(expand=True, fill="both", padx=10, pady=10)

    tree.heading("ID", text="ID")
    tree.heading("Número", text="Nº Ap.")
    tree.heading("Valor", text="Valor")
    tree.heading("ID Prédio", text="ID Prédio")
    tree.heading("Rua", text="Rua")
    tree.heading("Número Prédio", text="Nº Prédio")
    tree.heading("Bairro", text="Bairro")
    tree.heading("Cidade", text="Cidade")
    tree.heading("Estado", text="UF")

    tree.column("ID", width=60, anchor="center")
    tree.column("Número", width=80, anchor="center")
    tree.column("Valor", width=90, anchor="center")
    tree.column("ID Prédio", width=80, anchor="center")
    tree.column("Rua", width=180, anchor="center")
    tree.column("Número Prédio", width=90, anchor="center")
    tree.column("Bairro", width=120, anchor="center")
    tree.column("Cidade", width=120, anchor="center")
    tree.column("Estado", width=60, anchor="center")

    apartamentos = Db_Tools.Puxar_Apartamentos()
    for a in apartamentos:
        predio = a.predio
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

    def on_comprar():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("Aviso", "Selecione um apartamento para comprar.")
            return
        item = tree.item(selected[0])
        apartamento_id = item["values"][0]
        comprar_apartamento(apartamento_id)

    # Frame para botões lado a lado
    btn_frame = tk.Frame(content_frame, bg=BG_COLOR)
    btn_frame.pack(pady=10)

    btn_comprar = tk.Button(
        btn_frame, text="Comprar Apartamento Selecionado", command=on_comprar,
        bg=BTN_BG, fg=BTN_FG, font=FONT_BTN, bd=0, relief="flat", cursor="hand2",
        activebackground=BTN_HOVER, activeforeground="#223a5e", padx=10, pady=6
    )
    btn_comprar.pack(side="left", padx=8)
    btn_comprar.bind("<Enter>", on_enter)
    btn_comprar.bind("<Leave>", on_leave)

    btn_fechar = tk.Button(
        btn_frame, text="Fechar Tela", command=root.destroy,
        bg=BTN_BG, fg=BTN_FG, font=FONT_BTN, bd=0, relief="flat", cursor="hand2",
        activebackground=BTN_HOVER, activeforeground="#223a5e", padx=10, pady=6
    )
    btn_fechar.pack(side="left", padx=8)
    btn_fechar.bind("<Enter>", on_enter)
    btn_fechar.bind("<Leave>", on_leave)

def comprar_apartamento(apartamento_id):
    compra_win = tk.Toplevel(root)
    compra_win.title("Comprar Apartamento")
    compra_win.geometry("350x260")
    compra_win.resizable(False, False)
    compra_win.configure(bg=BG_COLOR)

    tk.Label(compra_win, text=f"Comprar Apartamento ID {apartamento_id}", font=FONT_BTN, bg=BG_COLOR, fg=TITLE_COLOR).pack(pady=10)
    tk.Label(compra_win, text="Digite o CPF do comprador:", font=FONT, bg=BG_COLOR).pack(pady=5)
    entry_cpf = tk.Entry(compra_win, font=FONT, width=25, bg="#f7fafc", relief="flat", highlightthickness=1, highlightbackground="#d1d5db")
    entry_cpf.pack(pady=5)

    tk.Label(compra_win, text="Digite a semana (1 a 52):", font=FONT, bg=BG_COLOR).pack(pady=5)
    entry_semana = tk.Entry(compra_win, font=FONT, width=10, bg="#f7fafc", relief="flat", highlightthickness=1, highlightbackground="#d1d5db")
    entry_semana.pack(pady=5)

    def confirmar_compra():
        cpf = entry_cpf.get().strip()
        semana = entry_semana.get().strip()
        if not cpf:
            messagebox.showerror("Erro", "Digite um CPF válido.")
            return
        if not semana.isdigit() or not (1 <= int(semana) <= 52):
            messagebox.showerror("Erro", "Digite uma semana válida (1 a 52).")
            return

        semana = int(semana)

        # Verifica se já existe aluguel para esse apartamento e semana
        alugueis = Db_Tools.Puxar_Alugueis()
        for aluguel in alugueis:
            if aluguel.id_apartamento == apartamento_id and aluguel.n_semana == semana:
                messagebox.showerror("Erro", f"Já existe aluguel para o apartamento {apartamento_id} na semana {semana}.")
                return

        # Busca o valor do apartamento e calcula o valor do aluguel
        apartamento = next((a for a in Db_Tools.Puxar_Apartamentos() if a.id == apartamento_id), None)
        if not apartamento:
            messagebox.showerror("Erro", "Apartamento não encontrado.")
            return
        valor_aluguel = round(apartamento.valor / 52, 2)

        try:
            resultado = Db_Tools.Comprar_Apartamento(apartamento_id, cpf, semana, valor_aluguel)
            if resultado and isinstance(resultado, int):
                messagebox.showinfo("Sucesso", f"Compra registrada com sucesso!\nSemana alugada: {semana}\nValor do aluguel: R$ {valor_aluguel}")
                compra_win.destroy()
            else:
                messagebox.showerror("Erro", "Falha ao registrar compra. Verifique o CPF, semana ou apartamento.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao registrar compra:\n{e}")

    btn_confirmar = tk.Button(
        compra_win, text="Confirmar Compra", command=confirmar_compra,
        bg=BTN_BG, fg=BTN_FG, font=FONT_BTN, bd=0, relief="flat", cursor="hand2",
        activebackground=BTN_HOVER, activeforeground="#223a5e", padx=10, pady=6
    )
    btn_confirmar.pack(pady=15)
    btn_confirmar.bind("<Enter>", on_enter)
    btn_confirmar.bind("<Leave>", on_leave)

listar_apartamentos()
root.mainloop()