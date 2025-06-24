import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
from database.database_tools import Db_Tools

BG_COLOR = "#f0f4f8"
ENTRY_BG = "#ffffff"
BTN_BG = "#4a90e2"
BTN_FG = "#ffffff"
FONT = ("Segoe UI", 14)

# Mostra a tela de cadastro de usuário
def show_cadastro():
    clear_frame(content_frame)  # Limpa o frame antes de desenhar os widgets
    tk.Label(content_frame, text="Cadastro de Usuário", bg=BG_COLOR, font=("Segoe UI", 24, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 30))

    # Campo para digitar o nome do usuário
    tk.Label(content_frame, text="Nome:", bg=BG_COLOR, font=FONT).grid(row=1, column=0, padx=20, pady=15, sticky="e")
    global entry_nome
    entry_nome = tk.Entry(content_frame, width=40, font=FONT, bg=ENTRY_BG)
    entry_nome.grid(row=1, column=1, padx=20, pady=15)

    # Campo para digitar o CPF do usuário
    tk.Label(content_frame, text="CPF:", bg=BG_COLOR, font=FONT).grid(row=2, column=0, padx=20, pady=15, sticky="e")
    global entry_cpf
    entry_cpf = tk.Entry(content_frame, width=40, font=FONT, bg=ENTRY_BG)
    entry_cpf.grid(row=2, column=1, padx=20, pady=15)

    # Campo para digitar a data de nascimento do usuário
    tk.Label(content_frame, text="Data de Nascimento\n(YYYY-MM-DD):", bg=BG_COLOR, font=FONT).grid(row=3, column=0, padx=20, pady=15, sticky="e")
    global entry_data
    entry_data = tk.Entry(content_frame, width=40, font=FONT, bg=ENTRY_BG)
    entry_data.grid(row=3, column=1, padx=20, pady=15)

    # Campo para digitar o e-mail do usuário
    tk.Label(content_frame, text="Email:", bg=BG_COLOR, font=FONT).grid(row=4, column=0, padx=20, pady=15, sticky="e")
    global entry_email
    entry_email = tk.Entry(content_frame, width=40, font=FONT, bg=ENTRY_BG)
    entry_email.grid(row=4, column=1, padx=20, pady=15)

    # Botão para cadastrar o usuário no banco
    btn_cadastrar = tk.Button(
        content_frame, text="Cadastrar", command=cadastrar_usuario,
        bg=BTN_BG, fg=BTN_FG, font=("Segoe UI", 16, "bold"), width=25, relief="raised", bd=2, activebackground="#357ab8"
    )
    btn_cadastrar.grid(row=5, column=0, columnspan=2, pady=40)

# Mostra a tela de listagem de usuários e permite deletar por ID
def show_usuarios():
    clear_frame(content_frame)
    tk.Label(content_frame, text="Usuários Cadastrados", bg=BG_COLOR, font=("Segoe UI", 24, "bold")).pack(pady=(0, 20))

    # Frame para campo de deletar usuário por ID
    top_frame = tk.Frame(content_frame, bg=BG_COLOR)
    top_frame.pack(fill="x", padx=20, pady=(0, 10))

    # Campo para digitar o ID do usuário a ser deletado
    tk.Label(top_frame, text="ID para deletar:", bg=BG_COLOR, font=FONT).pack(side="left")
    entry_id_delete = tk.Entry(top_frame, width=8, font=FONT, bg=ENTRY_BG)
    entry_id_delete.pack(side="left", padx=8)

    # Função para deletar o usuário do banco
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

    # Botão para deletar usuário selecionado
    btn_deletar = tk.Button(top_frame, text="Deletar", command=deletar_usuario, bg="#e63946", fg="#fff", font=FONT, bd=0, padx=15, pady=2, activebackground="#b71c1c")
    btn_deletar.pack(side="left", padx=8)

    # Tabela que mostra todos os usuários cadastrados
    tree = ttk.Treeview(content_frame, columns=("ID", "Nome", "CPF", "Nascimento", "Email"), show="headings", height=15)
    tree.pack(expand=True, fill="both", padx=20, pady=10)

    # Define os títulos das colunas e centraliza o texto
    for col in ("ID", "Nome", "CPF", "Nascimento", "Email"):
        tree.heading(col, text=col)
        tree.column(col, anchor="center")

    # Busca todos os usuários do banco e insere na tabela
    usuarios = Db_Tools.Puxar_Usuarios()
    for u in usuarios:
        tree.insert("", "end", values=(u.id, u.nome, u.cpf, u.data_nascimento, u.email))

# Limpa todos os widgets de um frame (usado para trocar de tela)
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# Função chamada ao clicar no botão "Cadastrar" para salvar usuário no banco
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

# Configura a janela principal do sistema de usuários
root = tk.Tk()
root.title("Sistema de Aluguéis")
root.configure(bg=BG_COLOR)
root.geometry("1200x800")
root.resizable(False, False)

# Cria a navbar para navegar entre cadastro e listagem de usuários
navbar = tk.Frame(root, bg="#22223b", height=60)
navbar.pack(side="top", fill="x")

# Botão para ir para tela de cadastro de usuário
btn_cadastro_nav = tk.Button(navbar, text="Cadastrar Usuário", command=show_cadastro, bg="#22223b", fg="#fff", font=FONT, bd=0, activebackground="#4a90e2", activeforeground="#fff", padx=30, pady=10, cursor="hand2")
btn_cadastro_nav.pack(side="left", padx=10, pady=10)

# Botão para ir para tela de listagem de usuários
btn_usuarios_nav = tk.Button(navbar, text="Puxar Usuários", command=show_usuarios, bg="#22223b", fg="#fff", font=FONT, bd=0, activebackground="#4a90e2", activeforeground="#fff", padx=30, pady=10, cursor="hand2")
btn_usuarios_nav.pack(side="left", padx=10, pady=10)

# Frame central onde as telas de cadastro e listagem aparecem
content_frame = tk.Frame(root, bg=BG_COLOR)
content_frame.pack(expand=True, fill="both")

# Mostra a tela de cadastro ao iniciar o programa
show_cadastro()

root.mainloop()