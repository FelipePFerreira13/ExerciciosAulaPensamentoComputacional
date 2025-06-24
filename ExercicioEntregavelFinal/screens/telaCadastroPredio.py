import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import messagebox, ttk
from database.database_tools import Db_Tools

# Paleta de cores e fontes padrão do sistema
BG_COLOR = "#e9eef6"
CARD_COLOR = "#ffffff"
BTN_BG = "#223a5e"
BTN_FG = "#fffbe7"
BTN_HOVER = "#e9b949"
TITLE_COLOR = "#223a5e"
DESC_COLOR = "#FFFFFF"
FONT_TITLE = ("Segoe UI", 28, "bold")
FONT_DESC = ("Segoe UI", 13, "italic")
FONT_BTN = ("Segoe UI", 15, "bold")
FONT = ("Segoe UI", 14)

# Criação da janela principal da tela de cadastro
root = tk.Tk()
root.title("Cadastro de Prédio")
root.configure(bg=BG_COLOR)
root.state('zoomed')
root.resizable(False, False)

# Função para efeito hover nos botões
def on_enter(e):
    e.widget['background'] = BTN_HOVER
    e.widget['fg'] = "#223a5e"

def on_leave(e):
    e.widget['background'] = BTN_BG
    e.widget['fg'] = BTN_FG

# Fecha a tela de cadastro e volta para tela inicial
def voltar_para_principal():
    root.destroy()

# Frame central para os formulários e tabelas
card = tk.Frame(root, bg=CARD_COLOR)
card.place(relx=0.5, rely=0.5, anchor="center")

# Exibe o formulário de cadastro de prédio
def show_cadastro():
    clear_frame(card)
    tk.Label(
        card, text="Cadastro de Prédio", bg=CARD_COLOR, fg=TITLE_COLOR, font=FONT_TITLE
    ).grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky="n")

    # Campo para digitar logradouro
    tk.Label(card, text="Logradouro:", bg=CARD_COLOR, font=FONT, anchor="e").grid(row=1, column=0, padx=(30,10), pady=10, sticky="e")
    global entry_rua
    entry_rua = tk.Entry(card, width=32, font=FONT, bg="#f7fafc", relief="flat", highlightthickness=1, highlightbackground="#d1d5db")
    entry_rua.grid(row=1, column=1, padx=(0,30), pady=10, sticky="w")

    # Campo para digitar número do prédio
    tk.Label(card, text="Número do Prédio:", bg=CARD_COLOR, font=FONT, anchor="e").grid(row=2, column=0, padx=(30,10), pady=10, sticky="e")
    global entry_numero
    entry_numero = tk.Entry(card, width=32, font=FONT, bg="#f7fafc", relief="flat", highlightthickness=1, highlightbackground="#d1d5db")
    entry_numero.grid(row=2, column=1, padx=(0,30), pady=10, sticky="w")

    # Campo para digitar bairro
    tk.Label(card, text="Bairro:", bg=CARD_COLOR, font=FONT, anchor="e").grid(row=3, column=0, padx=(30,10), pady=10, sticky="e")
    global entry_bairro
    entry_bairro = tk.Entry(card, width=32, font=FONT, bg="#f7fafc", relief="flat", highlightthickness=1, highlightbackground="#d1d5db")
    entry_bairro.grid(row=3, column=1, padx=(0,30), pady=10, sticky="w")

    # Campo para digitar cidade
    tk.Label(card, text="Cidade:", bg=CARD_COLOR, font=FONT, anchor="e").grid(row=4, column=0, padx=(30,10), pady=10, sticky="e")
    global entry_cidade
    entry_cidade = tk.Entry(card, width=32, font=FONT, bg="#f7fafc", relief="flat", highlightthickness=1, highlightbackground="#d1d5db")
    entry_cidade.grid(row=4, column=1, padx=(0,30), pady=10, sticky="w")

    # Campo para digitar estado
    tk.Label(card, text="Estado:", bg=CARD_COLOR, font=FONT, anchor="e").grid(row=5, column=0, padx=(30,10), pady=10, sticky="e")
    global entry_estado
    entry_estado = tk.Entry(card, width=32, font=FONT, bg="#f7fafc", relief="flat", highlightthickness=1, highlightbackground="#d1d5db")
    entry_estado.grid(row=5, column=1, padx=(0,30), pady=10, sticky="w")

    # Botão para cadastrar prédio no banco
    btn_cadastrar = tk.Button(
        card, text="Cadastrar", command=cadastrar_predio,
        bg=BTN_BG, fg=BTN_FG, font=FONT_BTN, bd=0, relief="flat", cursor="hand2",
        activebackground=BTN_HOVER, activeforeground="#223a5e", padx=10, pady=6
    )
    btn_cadastrar.grid(row=6, column=0, columnspan=2, pady=30)
    btn_cadastrar.bind("<Enter>", on_enter)
    btn_cadastrar.bind("<Leave>", on_leave)

    # Botão para ir para a tela de prédios (fica embaixo)
    nav_frame = tk.Frame(card, bg=CARD_COLOR)
    nav_frame.grid(row=7, column=0, columnspan=2, pady=(40, 10))

    btn_visualizar = tk.Button(
        nav_frame, text="Visualizar Prédios", command=show_predios,
        bg=BTN_BG, fg=BTN_FG, font=FONT_BTN, bd=0, relief="flat", cursor="hand2",
        activebackground=BTN_HOVER, activeforeground="#223a5e", padx=10, pady=4
    )
    btn_visualizar.pack(side="left", padx=20)
    btn_visualizar.bind("<Enter>", on_enter)
    btn_visualizar.bind("<Leave>", on_leave)

# Exibe a lista de prédios cadastrados e permite deletar pelo ID
def show_predios():
    clear_frame(card)
    tk.Label(card, text="Prédios Cadastrados", bg=CARD_COLOR, fg=TITLE_COLOR, font=FONT_TITLE).pack(pady=(0, 20))

    # Área para digitar o ID e deletar prédio
    top_frame = tk.Frame(card, bg=CARD_COLOR)
    top_frame.pack(fill="x", padx=20, pady=(0, 10))

    tk.Label(top_frame, text="ID para deletar:", bg=CARD_COLOR, font=FONT).pack(side="left")
    entry_id_delete = tk.Entry(top_frame, width=8, font=FONT, bg="#f7fafc", relief="flat", highlightthickness=1, highlightbackground="#d1d5db")
    entry_id_delete.pack(side="left", padx=8)

    # Botão para deletar prédio pelo ID
    def deletar_predio():
        try:
            predio_id = int(entry_id_delete.get())
            if Db_Tools.Deletar_Predio(predio_id):
                messagebox.showinfo("Sucesso", f"Prédio ID {predio_id} deletado!")
                show_predios()
            else:
                messagebox.showwarning("Aviso", "ID não encontrado.")
        except ValueError:
            messagebox.showerror("Erro", "Digite um ID válido.")

    btn_deletar = tk.Button(top_frame, text="Deletar", command=deletar_predio,
        bg="#e63946", fg="#fff", font=FONT, bd=0, padx=15, pady=2, activebackground="#b71c1c"
    )
    btn_deletar.pack(side="left", padx=8)

    # Tabela com todos os prédios cadastrados
    tree = ttk.Treeview(card, columns=("ID", "Logradouro", "Número", "Bairro", "Cidade", "Estado"), show="headings", height=15)
    tree.pack(expand=True, fill="both", padx=20, pady=10)

    for col in ("ID", "Logradouro", "Número", "Bairro", "Cidade", "Estado"):
        tree.heading(col, text=col)
        tree.column(col, anchor="center")

    predios = Db_Tools.Puxar_Predios()
    for p in predios:
        tree.insert("", "end", values=(p.id, p.rua, p.numero, p.bairro, p.cidade, p.estado))

    # Botões de navegação
    nav_frame = tk.Frame(card, bg=CARD_COLOR)
    nav_frame.pack(pady=(40, 10))

    btn_cadastro_area = tk.Button(
        nav_frame, text="Área de Cadastro", command=show_cadastro,
        bg=BTN_BG, fg=BTN_FG, font=FONT_BTN, bd=0, relief="flat", cursor="hand2",
        activebackground=BTN_HOVER, activeforeground="#223a5e", padx=10, pady=4
    )
    btn_cadastro_area.pack(side="left", padx=20)
    btn_cadastro_area.bind("<Enter>", on_enter)
    btn_cadastro_area.bind("<Leave>", on_leave)

    # Botão para abrir o cadastro de apartamento
    def abrir_cadastro_apartamento():
        os.system('python screens/telaCadastroApartamento.py')

    btn_cadastro_apartamento = tk.Button(
        nav_frame, text="Cadastrar Apartamento", command=abrir_cadastro_apartamento,
        bg=BTN_BG, fg=BTN_FG, font=FONT_BTN, bd=0, relief="flat", cursor="hand2",
        activebackground=BTN_HOVER, activeforeground="#223a5e", padx=10, pady=4
    )
    btn_cadastro_apartamento.pack(side="left", padx=20)
    btn_cadastro_apartamento.bind("<Enter>", on_enter)
    btn_cadastro_apartamento.bind("<Leave>", on_leave)

# Limpa todos os widgets do frame central (usado para trocar de tela)
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# Função para cadastrar prédio no banco de dados
def cadastrar_predio():
    rua = entry_rua.get()
    numero = entry_numero.get()
    bairro = entry_bairro.get()
    cidade = entry_cidade.get()
    estado = entry_estado.get()
    try:
        Db_Tools.Criar_Predio(rua, numero, bairro, cidade, estado)
        messagebox.showinfo("Sucesso", "Prédio cadastrado com sucesso!")
        entry_rua.delete(0, tk.END)
        entry_numero.delete(0, tk.END)
        entry_bairro.delete(0, tk.END)
        entry_cidade.delete(0, tk.END)
        entry_estado.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao cadastrar prédio:\n{e}")

# Botão fixo no topo para voltar à tela inicial
btn_voltar = tk.Button(
    root, text="Retornar à Tela Inicial", command=voltar_para_principal,
    bg=BTN_BG, fg=BTN_FG, font=FONT_BTN, bd=0, relief="flat", cursor="hand2",
    activebackground=BTN_HOVER, activeforeground="#223a5e", padx=10, pady=4
)
btn_voltar.place(x=30, y=30)
btn_voltar.bind("<Enter>", on_enter)
btn_voltar.bind("<Leave>", on_leave)

# Mostra a tela de cadastro ao iniciar
show_cadastro()
root.mainloop()