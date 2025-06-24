import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from database.database_tools import Db_Tools
import random
import webbrowser

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

    # Remova as colunas "ID" e "ID Prédio" da interface
    tree = ttk.Treeview(
        content_frame,
        columns=("Número", "Valor", "Rua", "Número Prédio", "Bairro", "Cidade", "Estado"),
        show="headings",
        height=25
    )
    tree.pack(expand=True, fill="both", padx=10, pady=10)

    tree.heading("Número", text="Nº Ap.")
    tree.heading("Valor", text="Valor")
    tree.heading("Rua", text="Rua")
    tree.heading("Número Prédio", text="Nº Prédio")
    tree.heading("Bairro", text="Bairro")
    tree.heading("Cidade", text="Cidade")
    tree.heading("Estado", text="UF")

    tree.column("Número", width=80, anchor="center")
    tree.column("Valor", width=90, anchor="center")
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
            iid=str(a.id),  # Use o ID do apartamento como iid
            values=(
                a.numero_apartamento,
                a.valor,
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
        apartamento_id = int(selected[0])  # O iid é o ID do apartamento
        comprar_apartamento(apartamento_id)

    def on_ver_google():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("Aviso", "Selecione um apartamento para visualizar no Google.")
            return
        apartamento_id = int(selected[0])  # O iid é o ID do apartamento
        apartamento = next((a for a in Db_Tools.Puxar_Apartamentos() if a.id == apartamento_id), None)
        if apartamento and hasattr(apartamento, "link_google") and apartamento.link_google:
            webbrowser.open(apartamento.link_google)
        else:
            messagebox.showerror("Erro", "Link do Google não encontrado para este apartamento.")

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

    btn_google = tk.Button(
        btn_frame, text="Ver no Google", command=on_ver_google,
        bg="#4285F4", fg="#fff", font=FONT_BTN, bd=0, relief="flat", cursor="hand2",
        activebackground="#3367D6", activeforeground="#fff", padx=10, pady=6
    )
    btn_google.pack(side="left", padx=8)

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
    compra_win.geometry("600x520")  # <-- Aumente aqui o tamanho da janela
    compra_win.resizable(False, False)
    compra_win.configure(bg=BG_COLOR)
    compra_win.grab_set()  # Mantém a janela modal/fixa

    frame = tk.Frame(compra_win, bg=BG_COLOR)
    frame.pack(expand=True, fill="both", padx=40, pady=25)

    tk.Label(
        frame, text=f"Comprar Apartamento ID {apartamento_id}",
        font=("Segoe UI", 18, "bold"), bg=BG_COLOR, fg=TITLE_COLOR
    ).grid(row=0, column=0, columnspan=2, pady=(0, 20))

    # Buscar valor do apartamento e calcular valor do aluguel
    apartamento = next((a for a in Db_Tools.Puxar_Apartamentos() if a.id == apartamento_id), None)
    if apartamento:
        valor_aluguel = round(apartamento.valor / 52, 2)
        valor_texto = f"Valor da semana: R$ {valor_aluguel:.2f}"
    else:
        valor_texto = "Valor não encontrado"

    # Exibir valor do aluguel
    tk.Label(
        frame, text=valor_texto,
        font=("Segoe UI", 15, "bold"), bg=BG_COLOR, fg="#27ae60"
    ).grid(row=1, column=0, columnspan=2, pady=(0, 10))

    # CPF
    tk.Label(frame, text="CPF do comprador:", font=FONT, bg=BG_COLOR, anchor="w").grid(
        row=2, column=0, sticky="e", pady=8, padx=(0, 8))
    entry_cpf = tk.Entry(frame, font=FONT, width=28, bg="#f7fafc", relief="flat",
                         highlightthickness=1, highlightbackground="#d1d5db")
    entry_cpf.grid(row=2, column=1, pady=8, sticky="w")

    # Semana
    tk.Label(frame, text="Semana (1 a 52):", font=FONT, bg=BG_COLOR, anchor="w").grid(
        row=3, column=0, sticky="e", pady=8, padx=(0, 8))
    entry_semana = tk.Entry(frame, font=FONT, width=13, bg="#f7fafc", relief="flat",
                           highlightthickness=1, highlightbackground="#d1d5db")
    entry_semana.grid(row=3, column=1, pady=8, sticky="w")

    # Cartão
    tk.Label(frame, text="Número do Cartão:", font=FONT, bg=BG_COLOR, anchor="w").grid(
        row=4, column=0, sticky="e", pady=8, padx=(0, 8))
    entry_cartao = tk.Entry(frame, font=FONT, width=24, bg="#f7fafc", relief="flat",
                           highlightthickness=1, highlightbackground="#d1d5db")
    entry_cartao.grid(row=4, column=1, pady=8, sticky="w")

    # CVV
    tk.Label(frame, text="CVV:", font=FONT, bg=BG_COLOR, anchor="w").grid(
        row=5, column=0, sticky="e", pady=8, padx=(0, 8))
    entry_cvv = tk.Entry(frame, font=FONT, width=8, bg="#f7fafc", relief="flat",
                        highlightthickness=1, highlightbackground="#d1d5db")
    entry_cvv.grid(row=5, column=1, pady=8, sticky="w")

    # Ano de validade
    tk.Label(frame, text="Ano de Validade:", font=FONT, bg=BG_COLOR, anchor="w").grid(
        row=6, column=0, sticky="e", pady=8, padx=(0, 8))
    entry_ano = tk.Entry(frame, font=FONT, width=8, bg="#f7fafc", relief="flat",
                        highlightthickness=1, highlightbackground="#d1d5db")
    entry_ano.grid(row=6, column=1, pady=8, sticky="w")

    # Função para preencher cartão aleatório
    def usar_meu_cartao():
        numero_cartao = "".join([str(random.randint(0, 9)) for _ in range(16)])
        cvv = str(random.randint(100, 999))
        ano = str(random.randint(2025, 2032))
        entry_cartao.delete(0, tk.END)
        entry_cartao.insert(0, numero_cartao)
        entry_cvv.delete(0, tk.END)
        entry_cvv.insert(0, cvv)
        entry_ano.delete(0, tk.END)
        entry_ano.insert(0, ano)

    # Frame para botões lado a lado
    btns_frame = tk.Frame(frame, bg=BG_COLOR)
    btns_frame.grid(row=7, column=0, columnspan=2, pady=(18, 0))

    btn_usar_cartao = tk.Button(
        btns_frame, text="Usar meu Cartão", command=usar_meu_cartao,
        bg=BTN_BG, fg=BTN_FG, font=FONT, bd=0, relief="flat", cursor="hand2",
        activebackground=BTN_HOVER, activeforeground="#223a5e", width=16, height=1, padx=8, pady=8
    )
    btn_usar_cartao.pack(side="left", padx=10)
    btn_usar_cartao.bind("<Enter>", on_enter)
    btn_usar_cartao.bind("<Leave>", on_leave)

    def confirmar_compra():
        cpf = entry_cpf.get().strip()
        semana = entry_semana.get().strip()
        if not cpf:
            messagebox.showerror("Erro", "Digite um CPF válido.", parent=compra_win)
            entry_cpf.focus_set()
            return
        if not semana.isdigit() or not (1 <= int(semana) <= 52):
            messagebox.showerror("Erro", "Digite uma semana válida (1 a 52).", parent=compra_win)
            entry_semana.focus_set()
            return

        semana = int(semana)

        alugueis = Db_Tools.Puxar_Alugueis()
        for aluguel in alugueis:
            if aluguel.id_apartamento == apartamento_id and aluguel.n_semana == semana:
                messagebox.showerror("Erro", f"Já existe aluguel para o apartamento {apartamento_id} na semana {semana}.", parent=compra_win)
                entry_semana.focus_set()
                return

        apartamento = next((a for a in Db_Tools.Puxar_Apartamentos() if a.id == apartamento_id), None)
        if not apartamento:
            messagebox.showerror("Erro", "Apartamento não encontrado.", parent=compra_win)
            return
        valor_aluguel = round(apartamento.valor / 52, 2)

        try:
            resultado = Db_Tools.Comprar_Apartamento(apartamento_id, cpf, semana, valor_aluguel)
            if resultado and isinstance(resultado, int):
                messagebox.showinfo("Sucesso", f"Compra registrada com sucesso!\nSemana alugada: {semana}\nValor do aluguel: R$ {valor_aluguel}", parent=compra_win)
                compra_win.destroy()
            else:
                messagebox.showerror("Erro", "Falha ao registrar compra. Verifique o CPF, semana ou apartamento.", parent=compra_win)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao registrar compra:\n{e}", parent=compra_win)

    btn_confirmar = tk.Button(
        btns_frame, text="Confirmar Compra", command=confirmar_compra,
        bg="#27ae60", fg="#fff", font=FONT_BTN, bd=0, relief="flat", cursor="hand2",
        activebackground="#219150", activeforeground="#fff", width=18, height=1, padx=8, pady=8
    )
    btn_confirmar.pack(side="left", padx=10)
    btn_confirmar.bind("<Enter>", lambda e: btn_confirmar.config(bg="#219150"))
    btn_confirmar.bind("<Leave>", lambda e: btn_confirmar.config(bg="#27ae60"))

listar_apartamentos()
root.mainloop()