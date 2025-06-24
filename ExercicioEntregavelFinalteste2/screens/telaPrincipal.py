import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from PIL import Image, ImageTk

# Defino as cores e fontes que vou usar em toda a interface
BG_COLOR = "#e9eef6"         # Fundo principal (azul acinzentado claro)
CARD_COLOR = "#ffffff"       # Card central (branco)
BTN_BG = "#223a5e"           # Botão principal (azul escuro)
BTN_FG = "#fffbe7"           # Texto do botão (quase branco)
BTN_HOVER = "#e9b949"        # Hover do botão (dourado)
TITLE_COLOR = "#223a5e"      # Título (azul escuro)
DESC_COLOR = "#4a5568"       # Descrição (cinza escuro)
FONT_TITLE = ("Segoe UI", 36, "bold")
FONT_DESC = ("Segoe UI", 16, "italic")
FONT_BTN = ("Segoe UI", 15, "bold")  # Fonte menor para os botões

class TelaPrincipal:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("DomusShare")
        self.root.configure(bg=BG_COLOR)
        self.root.state('zoomed')
        self.root.resizable(False, False)

        # Crio o card central onde ficam os botões e textos principais
        card = tk.Frame(self.root, bg=CARD_COLOR, bd=0, relief="ridge", highlightthickness=0)
        card.place(relx=0.5, rely=0.5, anchor="center", width=600, height=700)

        # Carrega e exibe a logo acima do título DomusShare
        logo_path = os.path.join(os.path.dirname(__file__), "logo.png")
        logo_img = Image.open(logo_path)
        logo_img = logo_img.resize((200, 200), Image.LANCZOS)
        logo_tk = ImageTk.PhotoImage(logo_img)

        logo_label = tk.Label(card, image=logo_tk, bg=CARD_COLOR)
        logo_label.image = logo_tk  # Mantém referência
        logo_label.pack(pady=(40, 10))

        tk.Label(
            card,
            text="Gerencie apartamentos, usuários e aluguéis de forma simples, rápida e elegante.",
            bg=CARD_COLOR, fg=DESC_COLOR, font=FONT_DESC, wraplength=500, justify="center"
        ).pack(pady=(0, 40))

        # Botão para ir para tela de cadastro de usuário
        btn_cadastro = tk.Button(
            card, text="Cadastrar Usuário", command=self.abrir_cadastro_usuario,
            bg=BTN_BG, fg=BTN_FG, font=FONT_BTN, bd=0, relief="flat", cursor="hand2",
            activebackground=BTN_HOVER, activeforeground="#223a5e", padx=16, pady=6
        )
        btn_cadastro.pack(pady=8)
        btn_cadastro.bind("<Enter>", self.on_enter)
        btn_cadastro.bind("<Leave>", self.on_leave)

        # Botão para ir para tela de listagem de apartamentos
        btn_listar_apartamentos = tk.Button(
            card, text="Listar Apartamentos", command=self.abrir_listar_apartamentos,
            bg=BTN_BG, fg=BTN_FG, font=FONT_BTN, bd=0, relief="flat", cursor="hand2",
            activebackground=BTN_HOVER, activeforeground="#223a5e", padx=16, pady=6
        )
        btn_listar_apartamentos.pack(pady=8)
        btn_listar_apartamentos.bind("<Enter>", self.on_enter)
        btn_listar_apartamentos.bind("<Leave>", self.on_leave)

        # Botão para ir para tela de listagem de aluguéis
        btn_listar_alugueis = tk.Button(
            card, text="Listar Aluguéis", command=self.abrir_listar_alugueis,
            bg=BTN_BG, fg=BTN_FG, font=FONT_BTN, bd=0, relief="flat", cursor="hand2",
            activebackground=BTN_HOVER, activeforeground="#223a5e", padx=16, pady=6
        )
        btn_listar_alugueis.pack(pady=8)
        btn_listar_alugueis.bind("<Enter>", self.on_enter)
        btn_listar_alugueis.bind("<Leave>", self.on_leave)

        # Botão para finalizar o aplicativo (fecha a janela principal)
        btn_finalizar = tk.Button(
            card, text="Finalizar Aplicativo", command=self.root.destroy,
            bg=BTN_BG, fg=BTN_FG, font=FONT_BTN, bd=0, relief="flat", cursor="hand2",
            activebackground=BTN_HOVER, activeforeground="#223a5e", padx=16, pady=6
        )
        btn_finalizar.pack(pady=8)
        btn_finalizar.bind("<Enter>", self.on_enter)
        btn_finalizar.bind("<Leave>", self.on_leave)

    # Função para mudar cor do botão quando o mouse passa em cima
    def on_enter(self, e):
        e.widget['background'] = BTN_HOVER
        e.widget['fg'] = "#223a5e"

    # Função para voltar cor do botão ao normal quando o mouse sai
    def on_leave(self, e):
        e.widget['background'] = BTN_BG
        e.widget['fg'] = BTN_FG

    # Funções para abrir cada tela do sistema
    def abrir_cadastro_usuario(self):
        os.system('python screens/telaCadastroUsuario.py')

    def abrir_listar_apartamentos(self):
        os.system('python screens/telaApartamentos.py')

    def abrir_listar_alugueis(self):
        os.system('python screens/telaAlugueis.py')

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = TelaPrincipal()
    app.run()