import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import ttk
from database.database_tools import Db_Tools

# Definição das cores e fontes do sistema
BG_COLOR = "#e9eef6"
BTN_BG = "#223a5e"
BTN_FG = "#fffbe7"
BTN_HOVER = "#e9b949"
FONT = ("Segoe UI", 9)
HEADER_FONT = ("Segoe UI", 10, "bold")

# Criação da janela principal da tela de aluguéis
root = tk.Tk()
root.title("Lista de Aluguéis")
root.configure(bg=BG_COLOR)
root.state('zoomed')
root.resizable(True, True)

# Função para mudar cor do botão quando mouse passa em cima
def on_enter(e):
    e.widget['background'] = BTN_HOVER
    e.widget['fg'] = "#223a5e"

# Função para voltar cor do botão ao normal quando mouse sai
def on_leave(e):
    e.widget['background'] = BTN_BG
    e.widget['fg'] = BTN_FG

# Frame central onde vai a tabela
content_frame = tk.Frame(root, bg=BG_COLOR)
content_frame.pack(expand=True, fill="both", padx=0, pady=(0, 60))  # Adiciona espaço inferior para o filtro

# Limita o texto exibido nas células da tabela
def limitar_texto(texto, limite):
    texto = str(texto)
    return texto if len(texto) <= limite else texto[:limite-3] + "..."

# Monta e exibe a tabela de aluguéis
def listar_alugueis():
    # Limpa widgets antigos do frame antes de desenhar a tabela
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Título da tela
    tk.Label(content_frame, text="Aluguéis Realizados", bg=BG_COLOR, font=("Segoe UI", 20, "bold")).pack(pady=(0, 10))

    # Define as colunas da tabela
    columns = (
        "ID Aluguel", "Nome", "CPF", "E-mail", "Data Nasc.",
        "ID Ap.", "Nº Ap.", "Valor", "ID Prédio", "Rua", "Nº Prédio", "Bairro", "Cidade", "UF", "Semana"
    )

    # Cria a tabela (Treeview)
    tree = ttk.Treeview(
        content_frame,
        columns=columns,
        show="headings",
        height=20  # Reduz a altura da tabela para liberar espaço para o filtro
    )
    tree.pack(expand=True, fill="both", padx=10, pady=10)

    # Define largura de cada coluna
    col_widths = [
        60, 120, 80, 150, 80, 60, 60, 70, 60, 180, 70, 100, 100, 40, 60
    ]
    for col, width in zip(columns, col_widths):
        tree.heading(col, text=col, anchor="center")
        tree.column(col, anchor="center", width=width, minwidth=40)

    # Busca todos os aluguéis no banco e insere na tabela
    alugueis = Db_Tools.Puxar_Alugueis()
    for aluguel in alugueis:
        usuario = aluguel.usuarios
        apartamento = aluguel.apartamento
        predio = apartamento.predio if apartamento else None
        tree.insert(
            "",
            "end",
            values=(
                aluguel.id,
                limitar_texto(usuario.nome if usuario else "", 18),
                limitar_texto(usuario.cpf if usuario else "", 11),
                limitar_texto(usuario.email if usuario else "", 22),
                usuario.data_nascimento.strftime("%d/%m/%Y") if usuario else "",
                apartamento.id if apartamento else "",
                limitar_texto(apartamento.numero_apartamento if apartamento else "", 6),
                aluguel.valor,
                predio.id if predio else "",
                limitar_texto(predio.rua if predio else "", 25),
                limitar_texto(predio.numero if predio else "", 8),
                limitar_texto(predio.bairro if predio else "", 14),
                limitar_texto(predio.cidade if predio else "", 14),
                limitar_texto(predio.estado if predio else "", 2),
                aluguel.n_semana
            )
        )

    # Configura o estilo da tabela (fonte das linhas e do cabeçalho)
    style = ttk.Style()
    style.configure("Treeview", font=FONT, rowheight=22, background=BG_COLOR)
    style.configure("Treeview.Heading", font=HEADER_FONT)

# Mostra a tabela ao abrir a tela
listar_alugueis()

# Botão para retornar à tela inicial (fica no canto superior esquerdo)
btn_fechar = tk.Button(
    root, text="Retornar Tela Inicial", command=root.destroy,
    bg=BTN_BG, fg=BTN_FG, font=("Segoe UI", 13, "bold"), bd=0, relief="flat", cursor="hand2",
    activebackground=BTN_HOVER, activeforeground="#223a5e", padx=4, pady=1, width=18
)
btn_fechar.place(x=10, y=20) 
btn_fechar.bind("<Enter>", on_enter)
btn_fechar.bind("<Leave>", on_leave)

# Adiciona frame para filtro de valor no canto inferior esquerdo
filtro_frame = tk.Frame(root, bg=BG_COLOR)
filtro_frame.place(x=15, rely=0.975, anchor="sw")  # Subiu um pouco o filtro

tk.Label(
    filtro_frame, text="Filtrar por valor menor que:", bg=BG_COLOR, font=("Segoe UI", 12)
).pack(side="left", padx=(0, 5))

valor_var = tk.StringVar()
entry_valor = tk.Entry(filtro_frame, textvariable=valor_var, width=10, font=("Segoe UI", 12))
entry_valor.pack(side="left", padx=(0, 5))

def filtrar_alugueis():
    try:
        preco = float(valor_var.get())
    except ValueError:
        return  # Ignora se não for número
    for widget in content_frame.winfo_children():
        widget.destroy()
    tk.Label(content_frame, text=f"Aluguéis com valor menor que {preco}", bg=BG_COLOR, font=("Segoe UI", 20, "bold")).pack(pady=(0, 10))
    columns = (
        "ID Aluguel", "Nome", "CPF", "E-mail", "Data Nasc.",
        "ID Ap.", "Nº Ap.", "Valor", "ID Prédio", "Rua", "Nº Prédio", "Bairro", "Cidade", "UF", "Semana"
    )
    tree = ttk.Treeview(
        content_frame,
        columns=columns,
        show="headings",
        height=20  # Reduz a altura da tabela também no filtro
    )
    tree.pack(expand=True, fill="both", padx=10, pady=10)
    col_widths = [
        60, 120, 80, 150, 80, 60, 60, 70, 60, 180, 70, 100, 100, 40, 60
    ]
    for col, width in zip(columns, col_widths):
        tree.heading(col, text=col, anchor="center")
        tree.column(col, anchor="center", width=width, minwidth=40)
    alugueis = Db_Tools.Filtrar_Alugueis_Valor(preco)
    for aluguel in alugueis:
        usuario = aluguel.usuarios
        apartamento = aluguel.apartamento
        predio = apartamento.predio if apartamento else None
        tree.insert(
            "",
            "end",
            values=(
                aluguel.id,
                limitar_texto(usuario.nome if usuario else "", 18),
                limitar_texto(usuario.cpf if usuario else "", 11),
                limitar_texto(usuario.email if usuario else "", 22),
                usuario.data_nascimento.strftime("%d/%m/%Y") if usuario else "",
                apartamento.id if apartamento else "",
                limitar_texto(apartamento.numero_apartamento if apartamento else "", 6),
                aluguel.valor,
                predio.id if predio else "",
                limitar_texto(predio.rua if predio else "", 25),
                limitar_texto(predio.numero if predio else "", 8),
                limitar_texto(predio.bairro if predio else "", 14),
                limitar_texto(predio.cidade if predio else "", 14),
                limitar_texto(predio.estado if predio else "", 2),
                aluguel.n_semana
            )
        )
    style = ttk.Style()
    style.configure("Treeview", font=FONT, rowheight=22, background=BG_COLOR)
    style.configure("Treeview.Heading", font=HEADER_FONT)

btn_filtrar = tk.Button(
    filtro_frame, text="Filtrar", command=filtrar_alugueis,
    bg=BTN_BG, fg=BTN_FG, font=("Segoe UI", 11, "bold"), bd=0, relief="flat", cursor="hand2",
    activebackground=BTN_HOVER, activeforeground="#223a5e", padx=8, pady=2
)
btn_filtrar.pack(side="left")
btn_filtrar.bind("<Enter>", on_enter)
btn_filtrar.bind("<Leave>", on_leave)

# Botão para reiniciar o filtro e mostrar todos os aluguéis novamente
def resetar_filtro():
    valor_var.set("")
    listar_alugueis()

btn_resetar = tk.Button(
    filtro_frame, text="Limpar Filtro", command=resetar_filtro,
    bg=BTN_BG, fg=BTN_FG, font=("Segoe UI", 11, "bold"), bd=0, relief="flat", cursor="hand2",
    activebackground=BTN_HOVER, activeforeground="#223a5e", padx=8, pady=2
)
btn_resetar.pack(side="left", padx=(10, 0))
btn_resetar.bind("<Enter>", on_enter)
btn_resetar.bind("<Leave>", on_leave)

root.mainloop()