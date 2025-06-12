import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
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
root.title("Cadastro de Usuário")
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

# Exibe o formulário de cadastro de usuário
def show_cadastro():
    clear_frame(card)
    tk.Label(
        card, text="Cadastro de Usuário", bg=CARD_COLOR, fg=TITLE_COLOR, font=FONT_TITLE
    ).grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky="n")

    # Campo para digitar nome
    tk.Label(card, text="Nome:", bg=CARD_COLOR, font=FONT, anchor="e").grid(row=1, column=0, padx=(30,10), pady=10, sticky="e")
    global entry_nome
    entry_nome = tk.Entry(card, width=32, font=FONT, bg="#f7fafc", relief="flat", highlightthickness=1, highlightbackground="#d1d5db")
    entry_nome.grid(row=1, column=1, padx=(0,30), pady=10, sticky="w")

    # Campo para digitar CPF
    tk.Label(card, text="CPF:", bg=CARD_COLOR, font=FONT, anchor="e").grid(row=2, column=0, padx=(30,10), pady=10, sticky="e")
    global entry_cpf
    entry_cpf = tk.Entry(card, width=32, font=FONT, bg="#f7fafc", relief="flat", highlightthickness=1, highlightbackground="#d1d5db")
    entry_cpf.grid(row=2, column=1, padx=(0,30), pady=10, sticky="w")

    # Campo para digitar data de nascimento
    tk.Label(card, text="Data de Nascimento\n(YYYY-MM-DD):", bg=CARD_COLOR, font=FONT, anchor="e", justify="right").grid(row=3, column=0, padx=(30,10), pady=10, sticky="e")
    global entry_data
    entry_data = tk.Entry(card, width=32, font=FONT, bg="#f7fafc", relief="flat", highlightthickness=1, highlightbackground="#d1d5db")
    entry_data.grid(row=3, column=1, padx=(0,30), pady=10, sticky="w")

    # Campo para digitar email
    tk.Label(card, text="Email:", bg=CARD_COLOR, font=FONT, anchor="e").grid(row=4, column=0, padx=(30,10), pady=10, sticky="e")
    global entry_email
    entry_email = tk.Entry(card, width=32, font=FONT, bg="#f7fafc", relief="flat", highlightthickness=1, highlightbackground="#d1d5db")
    entry_email.grid(row=4, column=1, padx=(0,30), pady=10, sticky="w")

    # Botão para cadastrar usuário no banco
    btn_cadastrar = tk.Button(
        card, text="Cadastrar", command=cadastrar_usuario,
        bg=BTN_BG, fg=BTN_FG, font=FONT_BTN, bd=0, relief="flat", cursor="hand2",
        activebackground=BTN_HOVER, activeforeground="#223a5e", padx=10, pady=6
    )
    btn_cadastrar.grid(row=5, column=0, columnspan=2, pady=30)
    btn_cadastrar.bind("<Enter>", on_enter)
    btn_cadastrar.bind("<Leave>", on_leave)

    # Botão para ir para a tela de usuários (fica embaixo)
    nav_frame = tk.Frame(card, bg=CARD_COLOR)
    nav_frame.grid(row=6, column=0, columnspan=2, pady=(40, 10))

    btn_visualizar = tk.Button(
        nav_frame, text="Visualizar Usuários", command=show_usuarios,
        bg=BTN_BG, fg=BTN_FG, font=FONT_BTN, bd=0, relief="flat", cursor="hand2",
        activebackground=BTN_HOVER, activeforeground="#223a5e", padx=10, pady=4
    )
    btn_visualizar.pack(side="left", padx=20)
    btn_visualizar.bind("<Enter>", on_enter)
    btn_visualizar.bind("<Leave>", on_leave)

# Exibe a lista de usuários cadastrados e permite deletar pelo ID
def show_usuarios():
    clear_frame(card)
    tk.Label(card, text="Usuários Cadastrados", bg=CARD_COLOR, fg=TITLE_COLOR, font=FONT_TITLE).pack(pady=(0, 20))

    # Área para digitar o ID e deletar usuário
    top_frame = tk.Frame(card, bg=CARD_COLOR)
    top_frame.pack(fill="x", padx=20, pady=(0, 10))

    tk.Label(top_frame, text="ID para deletar:", bg=CARD_COLOR, font=FONT).pack(side="left")
    entry_id_delete = tk.Entry(top_frame, width=8, font=FONT, bg="#f7fafc", relief="flat", highlightthickness=1, highlightbackground="#d1d5db")
    entry_id_delete.pack(side="left", padx=8)

    # Botão para deletar usuário pelo ID
    def deletar_usuario():
        try:
            usuario_id = int(entry_id_delete.get())
            if Db_Tools.Deletar_Usuario(usuario_id):
                messagebox.showinfo("Sucesso", f"Usuário ID {usuario_id} deletado!")
                show_usuarios()
            else:
                messagebox.showwarning("Aviso", "ID não encontrado.")
        except ValueError:
            messagebox.showerror("Erro", "Digite um ID válido.")

    btn_deletar = tk.Button(top_frame, text="Deletar", command=deletar_usuario,
        bg="#e63946", fg="#fff", font=FONT, bd=0, padx=15, pady=2, activebackground="#b71c1c"
    )
    btn_deletar.pack(side="left", padx=8)

    # Tabela com todos os usuários cadastrados
    tree = ttk.Treeview(card, columns=("ID", "Nome", "CPF", "Nascimento", "Email"), show="headings", height=15)
    tree.pack(expand=True, fill="both", padx=20, pady=10)

    for col in ("ID", "Nome", "CPF", "Nascimento", "Email"):
        tree.heading(col, text=col)
        tree.column(col, anchor="center")

    usuarios = Db_Tools.Puxar_Usuarios()
    for u in usuarios:
        tree.insert("", "end", values=(u.id, u.nome, u.cpf, u.data_nascimento, u.email))

    # Botão para voltar para a tela de cadastro (fica embaixo)
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

# Limpa todos os widgets do frame central (usado para trocar de tela)
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# Função para cadastrar usuário no banco de dados
def cadastrar_usuario():
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    data_nascimento = entry_data.get()
    email = entry_email.get()
    try:
        data_nasc = datetime.strptime(data_nascimento, "%Y-%m-%d").date()
        Db_Tools.Criar_Usuario(nome, cpf, data_nasc, email)
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        entry_nome.delete(0, tk.END)
        entry_cpf.delete(0, tk.END)
        entry_data.delete(0, tk.END)
        entry_email.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao cadastrar usuário:\n{e}")

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