import tkinter as tk
from models.Veiculo import Veiculo

class Cadastro_Veiculos:
    
    
    def mostrar_opcao():
        rotulo.config(text=f"Escolheu: {opcao.get()}")

    def __init__(self):        

        janela = tk.Tk()
        janela.title("Cadastro de Veículo")
        janela.geometry("800x600")
        opcao = tk.StringVar(value=1)
        tk.Radiobutton(janela, text="Carro", variable=opcao, value=1).grid(row=1,column=2,pady=2)
        tk.Radiobutton(janela, text="Moto", variable=opcao, value=2).grid(row=1,column=3,pady=2)
        tk.Radiobutton(janela, text="Caminhão", variable=opcao, value=3).grid(row=1,column=4,pady=2)        
        entrada1 = tk.Entry(janela)
        entrada1.grid(row=2,column=4,pady=2)
        entrada2 = tk.Entry(janela)
        entrada2.grid(row=3,column=4,pady=2)
        entrada3 = tk.Entry(janela)
        entrada3.grid(row=4,column=4,pady=2)
        entrada4 = tk.Entry(janela)
        entrada4.grid(row=5,column=4,pady=2)
        i=2
        proprietarios = 1
        for prop in range(1,10):
            tk.Radiobutton(janela, text="Caminhão", variable=proprietarios, value=prop).grid(row=i,column=5,pady=2)        
            i+=1
        
        
        
        
        
        
        
        
        
        
        
        janela.mainloop()
            
            
    def get_entry_value(event):
        value = entrada.get()
        return value
