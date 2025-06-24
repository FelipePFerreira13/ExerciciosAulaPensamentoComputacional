import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from database.database_tools import Db_Tools

BG_COLOR = "#e9eef6"
CARD_COLOR = "#ffffff"
BTN_BG = "#223a5e"
BTN_FG = "#fffbe7"
BTN_HOVER = "#e9b949"
TITLE_COLOR = "#223a5e"
FONT_TITLE = ("Segoe UI", 28, "bold")
FONT = ("Segoe UI", 14)
FONT_BTN = ("Segoe UI", 15, "bold")

root = tk.Tk()
root.title("Cadastro de Apartamento")
root.configure(bg=BG_COLOR)
root.geometry("750x500")
root.resizable(False, False)

def on_enter(e):
    e.widget['background'] = BTN_HOVER
    e.widget['fg'] = "#223a5e"

def on_leave(e):
    e.widget['background'] = BTN_BG
    e.widget['fg'] = BTN_FG

frame = tk.Frame(root, bg=BG_COLOR)
frame.pack(expand=True, fill="both", padx=40, pady=30)

tk.Label(
    frame, text="Cadastrar Novo Apartamento",
    bg=BG_COLOR, fg=TITLE_COLOR, font=FONT_TITLE
).grid(row=0, column=0, columnspan=2, pady=(0, 20))

# Buscar prédios cadastrados
predios = Db_Tools.Puxar_Predios()
predio_dict = {f"{p.rua}, {p.numero} - {p.bairro}, {p.cidade}/{p.estado} (ID {p.id})": p.id for p in predios}
predio_nomes = list(predio_dict.keys())

tk.Label(frame, text="Selecione o Prédio:", font=FONT, bg=BG_COLOR).grid(row=1, column=0, sticky="e", pady=8, padx=(0, 8))
combo_predio = ttk.Combobox(frame, values=predio_nomes, font=FONT, width=38, state="readonly")
combo_predio.grid(row=1, column=1, pady=8, sticky="w")

tk.Label(frame, text="Número do Apartamento:", font=FONT, bg=BG_COLOR).grid(row=2, column=0, sticky="e", pady=8, padx=(0, 8))
entry_numero = tk.Entry(frame, font=FONT, width=20, bg="#f7fafc", relief="flat")
entry_numero.grid(row=2, column=1, pady=8, sticky="w")

tk.Label(frame, text="Valor (R$):", font=FONT, bg=BG_COLOR).grid(row=3, column=0, sticky="e", pady=8, padx=(0, 8))
entry_valor = tk.Entry(frame, font=FONT, width=20, bg="#f7fafc", relief="flat")
entry_valor.grid(row=3, column=1, pady=8, sticky="w")

tk.Label(frame, text="Link Google Maps:", font=FONT, bg=BG_COLOR).grid(row=4, column=0, sticky="e", pady=8, padx=(0, 8))
entry_link = tk.Entry(frame, font=FONT, width=38, bg="#f7fafc", relief="flat")
entry_link.grid(row=4, column=1, pady=8, sticky="w")

def cadastrar_apartamento():
    predio_nome = combo_predio.get()
    numero = entry_numero.get().strip()
    valor = entry_valor.get().strip()
    link = entry_link.get().strip()

    if not predio_nome:
        messagebox.showerror("Erro", "Selecione um prédio.")
        return
    if not numero.isdigit():
        messagebox.showerror("Erro", "Digite um número de apartamento válido.")
        entry_numero.focus_set()
        return
    try:
        valor_float = float(valor)
        if valor_float <= 0:
            raise ValueError
    except:
        messagebox.showerror("Erro", "Digite um valor válido para o apartamento.")
        entry_valor.focus_set()
        return
    if not link:
        messagebox.showerror("Erro", "Digite o link do Google Maps.")
        entry_link.focus_set()
        return

    id_predio = predio_dict[predio_nome]
    try:
        Db_Tools.Criar_Apartamento(id_predio, int(numero), valor_float, link)
        messagebox.showinfo("Sucesso", "Apartamento cadastrado com sucesso!")
        entry_numero.delete(0, tk.END)
        entry_valor.delete(0, tk.END)
        entry_link.delete(0, tk.END)
        combo_predio.set('')
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao cadastrar apartamento:\n{e}")

btn_cadastrar = tk.Button(
    frame, text="Cadastrar Apartamento", command=cadastrar_apartamento,
    bg=BTN_BG, fg=BTN_FG, font=FONT_BTN, bd=0, relief="flat", cursor="hand2",
    activebackground=BTN_HOVER, activeforeground="#223a5e", width=22, height=1, padx=8, pady=8
)
btn_cadastrar.grid(row=5, column=0, columnspan=2, pady=(22, 0))
btn_cadastrar.bind("<Enter>", on_enter)
btn_cadastrar.bind("<Leave>", on_leave)

def abrir_visualizar_apartamentos():
    # Nova janela para visualização e deleção de apartamentos
    win = tk.Toplevel(root)
    win.title("Apartamentos Cadastrados")
    win.configure(bg=BG_COLOR)
    win.geometry("1200x500")
    win.resizable(False, False)

    frame_ap = tk.Frame(win, bg=BG_COLOR)
    frame_ap.pack(padx=20, pady=20)

    tk.Label(
        frame_ap, text="Apartamentos Cadastrados",
        bg=BG_COLOR, fg=TITLE_COLOR, font=FONT_TITLE
    ).pack(pady=(0, 10))

    # Tabela de apartamentos
    tree = ttk.Treeview(
        frame_ap,
        columns=("ID", "Prédio", "Nº Ap.", "Valor", "Link"),
        show="headings",
        height=15,
        
    )
    tree.pack(expand=True, fill="both", padx=10, pady=10)

    tree.heading("ID", text="ID")
    tree.column("ID", width=40, stretch=False)
    tree.heading("Prédio", text="Prédio")
    tree.column("Prédio", width=400, stretch=False)
    tree.heading("Nº Ap.", text="Nº Ap.")
    tree.column("Nº Ap.", width=50, stretch=False)
    tree.heading("Valor", text="Valor (R$)")
    tree.column("Valor", width=120, stretch=False)
    tree.heading("Link", text="Google Maps")
    tree.column("Link", width=900, stretch=False)

    # Preencher tabela
    apartamentos = Db_Tools.Puxar_Apartamentos()
    predios = {p.id: p for p in Db_Tools.Puxar_Predios()}
    for ap in apartamentos:
        predio = predios.get(ap.id_predio)
        predio_str = f"{predio.rua}, {predio.numero} - {predio.bairro}, {predio.cidade}/{predio.estado}" if predio else "N/A"
        tree.insert("", "end", values=(ap.id, predio_str, ap.numero_apartamento, f"R$ {ap.valor:.2f}", ap.link_google))

    # Campo e botão para deletar apartamento
    del_frame = tk.Frame(frame_ap, bg=BG_COLOR)
    del_frame.pack(pady=(10, 0))

    tk.Label(del_frame, text="ID para deletar:", bg=BG_COLOR, font=FONT).pack(side="left")
    entry_del = tk.Entry(del_frame, width=8, font=FONT, bg="#f7fafc", relief="flat")
    entry_del.pack(side="left", padx=8)

    def deletar_apartamento():
        try:
            ap_id = int(entry_del.get())
            if Db_Tools.Deletar_Apartamento(ap_id):
                messagebox.showinfo("Sucesso", f"Apartamento ID {ap_id} deletado!")
                win.destroy()
                abrir_visualizar_apartamentos()
            else:
                messagebox.showwarning("Aviso", "ID não encontrado.")
        except ValueError:
            messagebox.showerror("Erro", "Digite um ID válido.")

    btn_del = tk.Button(
        del_frame, text="Deletar", command=deletar_apartamento,
        bg="#e63946", fg="#fff", font=FONT_BTN, bd=0, padx=15, pady=2, activebackground="#b71c1c"
    )
    btn_del.pack(side="left", padx=8)

btn_visualizar = tk.Button(
    frame, text="Visualizar Apartamentos", command=abrir_visualizar_apartamentos,
    bg=BTN_BG, fg=BTN_FG, font=FONT_BTN, bd=0, relief="flat", cursor="hand2",
    activebackground=BTN_HOVER, activeforeground="#223a5e", width=22, height=1, padx=8, pady=8
)
btn_visualizar.grid(row=6, column=0, columnspan=2, pady=(12, 0))
btn_visualizar.bind("<Enter>", on_enter)
btn_visualizar.bind("<Leave>", on_leave)

root.mainloop()