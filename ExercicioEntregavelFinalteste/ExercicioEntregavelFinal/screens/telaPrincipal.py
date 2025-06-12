import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk

BG_COLOR = "#e3eafc"
BTN_BG = "#4a90e2"
BTN_FG = "#ffffff"
BTN_HOVER = "#357ab8"
FONT_TITLE = ("Segoe UI", 32, "bold")
FONT_BTN = ("Segoe UI", 18, "bold")

class TelaPrincipal:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tela Principal")
        self.root.configure(bg=BG_COLOR)
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        self.frame = tk.Frame(self.root, bg=BG_COLOR)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(
            self.frame, text="Sistema de Aluguéis", bg=BG_COLOR, fg="#22223b",
            font=FONT_TITLE
        ).pack(pady=(0, 60))

        btn_cadastro = tk.Button(
            self.frame, text="Cadastrar Usuário", command=self.abrir_cadastro_usuario,
            bg=BTN_BG, fg=BTN_FG, font=FONT_BTN, width=22, height=2, bd=0, relief="ridge",
            activebackground=BTN_HOVER, activeforeground=BTN_FG, cursor="hand2"
        )
        btn_cadastro.pack(pady=20)

        btn_listar_apartamentos = tk.Button(
            self.frame, text="Listar Apartamentos", command=self.abrir_listar_apartamentos,
            bg=BTN_BG, fg=BTN_FG, font=FONT_BTN, width=22, height=2, bd=0, relief="ridge",
            activebackground=BTN_HOVER, activeforeground=BTN_FG, cursor="hand2"
        )
        btn_listar_apartamentos.pack(pady=20)

        btn_listar_alugueis = tk.Button(
            self.frame, text="Listar Aluguéis", command=self.abrir_listar_alugueis,
            bg=BTN_BG, fg=BTN_FG, font=FONT_BTN, width=22, height=2, bd=0, relief="ridge",
            activebackground=BTN_HOVER, activeforeground=BTN_FG, cursor="hand2"
        )
        btn_listar_alugueis.pack(pady=20)

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