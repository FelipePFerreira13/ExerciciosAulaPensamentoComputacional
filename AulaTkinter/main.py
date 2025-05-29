import tkinter as tk

lista = list()
def mostrar_opcao():
    
    texto = f"Escolheu: {opcao1.get()}"
    texto += f" {opcao2.get()}"
    texto += f" {opcao3.get()}"
    rotulo.config(text = texto)


def botao(x):
    global lista
    lista.append(x)
    if len(lista)>2:
        if lista[0] == 1:
            opcao1.set(False)
            lista.pop(0)
        elif lista[0] == 2:
            opcao2.set(False)
            lista.pop(0)
        elif lista[0] == 3:
            opcao3.set(False)
            lista.pop(0)
        
    mostrar_opcao()


janela = tk.Tk()
janela.title("Exemplo")
janela.geometry("800x600")
opcao1 = tk.BooleanVar()
opcao2 = tk.BooleanVar()
opcao3 = tk.BooleanVar()
tk.Radiobutton(janela, text="Opção A", variable=opcao1, value=True,command=botao(1)).pack()
tk.Radiobutton(janela, text="Opção B", variable=opcao2, value=True,command=botao(2)).pack()
tk.Radiobutton(janela, text="Opção C", variable=opcao3, value=True,command=botao(3)).pack()
rotulo = tk.Label(janela, text="Escolheu: A")
rotulo.pack(pady=10)
janela.mainloop()
