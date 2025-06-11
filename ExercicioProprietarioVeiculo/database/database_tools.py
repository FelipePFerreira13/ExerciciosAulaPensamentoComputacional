import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.database import Usuario, Base, Carro, Moto, Caminhao
from datetime import date

engine = create_engine('sqlite:///database/database.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

class Db_Tools:
    
    def Criar_Usuario(nome: str, cpf: str) -> Usuario:
        
        novo_usuario = Usuario(nome=nome, cpf=cpf)
        
        session.add(novo_usuario)
        session.commit()
        return novo_usuario
    
    def Criar_Carro(placa: str, marca: str, modelo: str, ano: int, num_portas: int, id_proprietario: int) -> Carro:
        
        novo_carro = Carro(placa=placa, marca=marca, modelo=modelo, ano=ano, num_portas=num_portas, id_proprietario=id_proprietario)
        
        session.add(novo_carro)
        session.commit()
        return novo_carro
    
    def Criar_Caminhao(placa: str, marca: str, modelo: str, ano: int, capacidade_carga: int, id_proprietario: int) -> Carro:
        
        novo_caminhao = Caminhao(placa=placa, marca=marca, modelo=modelo, ano=ano, capacidade_carga=capacidade_carga, id_proprietario=id_proprietario)
        
        session.add(novo_caminhao)
        session.commit()
        return novo_caminhao
    
    def Criar_Moto(placa: str, marca: str, modelo: str, ano: int, cilindrada: int, id_proprietario: int) -> Moto:
        
        novo_moto = Moto(placa=placa, marca=marca, modelo=modelo, ano=ano, cilindrada=cilindrada, id_proprietario=id_proprietario)
        
        session.add(novo_moto)
        session.commit()
        return novo_moto
    
    def Listar_Usuarios():
        users = session.query(Usuario).all()
        # Retorna uma lista de tuplas (id, nome)
        return [(user.id, user.nome) for user in users]
    
    @staticmethod
    def Listar_Veiculos():
        # Exemplo para carros, adapte para motos/caminhões se quiser
        return [
            (v.placa, v.modelo, v.ano, v.marca, v.proprietario.nome if v.proprietario else "Sem proprietário")
            for v in session.query(Carro).all()
        ]

