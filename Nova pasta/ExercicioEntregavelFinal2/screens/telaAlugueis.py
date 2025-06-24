import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import ttk
from database.database_tools import Db_Tools

# Definições visuais
BG_COLOR = "#f0f4f8"
FONT = ("Segoe UI", 9)  # Fonte padrão para as linhas da tabela
HEADER_FONT = ("Segoe UI", 10, "bold")  # Fonte para o cabeçalho

# Cria a janela principal da tela de aluguéis
root = tk.Tk()
root.title("Lista de Aluguéis")
root.configure(bg=BG_COLOR)
root.state('zoomed')  # Deixa a janela maximizada
root.resizable(True, True)

# Frame central para colocar a tabela
content_frame = tk.Frame(root, bg=BG_COLOR)
content_frame.pack(expand=True, fill="both")

# Função para limitar o tamanho do texto exibido nas células
def limitar_texto(texto, limite):
    texto = str(texto)
    return texto if len(texto) <= limite else texto[:limite-3] + "..."

# Função que monta e exibe a tabela de aluguéis
def listar_alugueis():
    # Limpa widgets antigos do frame antes de desenhar a tabela
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Título da tela
    tk.Label(content_frame, text="Aluguéis Realizados", bg=BG_COLOR, font=("Segoe UI", 20, "bold")).pack(pady=(0, 10))

    # Definição das colunas da tabela
    columns = (
        "ID Aluguel", "Nome", "CPF", "E-mail", "Data Nasc.",
        "ID Ap.", "Nº Ap.", "Valor", "ID Prédio", "Rua", "Nº Prédio", "Bairro", "Cidade", "UF", "Semana"
    )

    # Cria a tabela (Treeview)
    tree = ttk.Treeview(
        content_frame,
        columns=columns,
        show="headings",
        height=25
    )
    tree.pack(expand=True, fill="both", padx=10, pady=10)

    # Define a largura de cada coluna para caber tudo na tela
    col_widths = [
        60,   # ID Aluguel
        120,  # Nome
        80,   # CPF
        150,  # E-mail
        80,   # Data Nasc.
        60,   # ID Ap.
        60,   # Nº Ap.
        70,   # Valor
        60,   # ID Prédio
        180,  # Rua
        70,   # Nº Prédio
        100,  # Bairro
        100,  # Cidade
        40,   # UF
        60    # Semana
    ]

    # Configura os cabeçalhos e larguras das colunas
    for col, width in zip(columns, col_widths):
        tree.heading(col, text=col, anchor="center")
        tree.column(col, anchor="center", width=width, minwidth=40)

    # Busca todos os aluguéis no banco e insere na tabela
    alugueis = Db_Tools.Filtrar_Alugueis_Valor(150000)
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

# Chama a função para exibir a tabela ao abrir a tela
listar_alugueis()
root.mainloop()