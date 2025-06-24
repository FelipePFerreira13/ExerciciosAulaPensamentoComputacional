from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.database import Usuario, Predio, Apartamento, Aluguel, Base
from datetime import date

# Crio o engine e inicializo o banco de dados SQLite
engine = create_engine('sqlite:///database/database.db')
Base.metadata.create_all(engine)

# Crio a sessão para manipular o banco
Session = sessionmaker(bind=engine)
session = Session()

class Db_Tools:
    # Cria um novo usuário no banco
    def Criar_Usuario(nome: str, cpf: str, data_nascimento: date, email: str) -> Usuario:
        novo_usuario = Usuario(nome=nome, cpf=cpf, data_nascimento=data_nascimento, email=email)
        session.add(novo_usuario)
        session.commit()
        return novo_usuario

    # Busca todos os usuários cadastrados
    @staticmethod
    def Puxar_Usuarios():
        return session.query(Usuario).all()

    # Deleta um usuário pelo ID
    @staticmethod
    def Deletar_Usuario(usuario_id: int):
        usuario = session.query(Usuario).filter_by(id=usuario_id).first()
        if usuario:
            session.delete(usuario)
            session.commit()
            return True
        return False

    # Busca todos os apartamentos cadastrados
    @staticmethod
    def Puxar_Apartamentos():
        return session.query(Apartamento).all()

    # Realiza a compra/aluguel de um apartamento para o CPF informado
    @staticmethod
    def Comprar_Apartamento(apartamento_id: int, cpf: str):
        usuario = session.query(Usuario).filter_by(cpf=cpf).first()
        if not usuario:
            return False
        apartamento = session.query(Apartamento).filter_by(id=apartamento_id).first()
        if not apartamento:
            return False
        # Descobre quais semanas já estão ocupadas para esse apartamento
        semanas_ocupadas = session.query(Aluguel.n_semana).filter_by(id_apartamento=apartamento_id).all()
        semanas_ocupadas = [s[0] for s in semanas_ocupadas]
        n_semana = 1
        # Procura a próxima semana livre
        while n_semana in semanas_ocupadas:
            n_semana += 1
        # Cria o aluguel para a próxima semana disponível
        novo_aluguel = Aluguel(
            id_apartamento=apartamento_id,
            id_usuario=usuario.id,
            n_semana=n_semana,
            valor=apartamento.valor
        )
        session.add(novo_aluguel)
        session.commit()
        return n_semana

    # Busca todos os aluguéis realizados
    @staticmethod
    def Puxar_Alugueis():
        from database.database import Aluguel
        return session.query(Aluguel).all()
    
    
    # Busca todos os aluguéis realizados
    @staticmethod
    def Filtrar_Alugueis_Valor(preco):
        from database.database import Aluguel
        return session.query(Aluguel).filter(Aluguel.valor < preco)

