import tkinter as tk

class Tela_Principal:
    
    
    def mostrar_opcao():
        rotulo.config(text=f"Escolheu: {opcao.get()}")

    def __init__(self):        

        janela = tk.Tk()
        janela.title("Cadastro de Veículo")
        janela.geometry("800x600")
        opcao = tk.StringVar(value=1)
        tk.Radiobutton(janela, text="Carro", variable=opcao, value=1).pack()
        tk.Radiobutton(janela, text="Moto", variable=opcao, value=2).pack()
        tk.Radiobutton(janela, text="Caminhão", variable=opcao, value=3).pack()        
        entrada1 = tk.Entry(janela)
        entrada1.pack()
        entrada1 = tk.Entry(janela)
        entrada1.pack()
        entrada1 = tk.Entry(janela)
        entrada1.pack()
        entrada1 = tk.Entry(janela)
        entrada1.pack()
        rotulo = tk.Label(janela, text="Escolheu: Carro")
        rotulo.pack(pady=10)
        janela.mainloop()
        
        
    def get_entry_value(event):
        value = entrada.get()
        return value
