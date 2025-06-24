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
    
    # Cria um novo predio no banco
    def Criar_Predio(rua: str, numero: str, bairro: str, cidade: str, estado: str) -> Predio:
        novo_predio = Predio(rua=rua, numero=numero, bairro=bairro, cidade=cidade, estado=estado)
        session.add(novo_predio)
        session.commit()
        return novo_predio
    
    

    # Busca todos os usuários cadastrados
    @staticmethod
    def Puxar_Usuarios():
        return session.query(Usuario).all()

    # Busca todos os usuários cadastrados
    @staticmethod
    def Puxar_Predios():
        return session.query(Predio).all()

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

    # Realiza a compra/aluguel de um apartamento para o CPF informado, semana e valor
    @staticmethod
    def Comprar_Apartamento(apartamento_id: int, cpf: str, semana: int, valor_aluguel: float):
        usuario = session.query(Usuario).filter_by(cpf=cpf).first()
        if not usuario:
            return False
        apartamento = session.query(Apartamento).filter_by(id=apartamento_id).first()
        if not apartamento:
            return False
        # Verifica se a semana já está ocupada para esse apartamento
        semana_ocupada = session.query(Aluguel).filter_by(id_apartamento=apartamento_id, n_semana=semana).first()
        if semana_ocupada:
            return False  # Semana já ocupada
        # Cria o aluguel para a semana informada
        novo_aluguel = Aluguel(
            id_apartamento=apartamento_id,
            id_usuario=usuario.id,
            n_semana=semana,
            valor=valor_aluguel
        )
        session.add(novo_aluguel)
        session.commit()
        return novo_aluguel.id  # Ou True, se preferir

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

    @staticmethod
    def Listar_Alugueis_Valor(ordem):
        from database.database import Aluguel
        if ordem == 1:
            return session.query(Aluguel).order_by(Aluguel.valor.desc())
        elif ordem == 0:
            return session.query(Aluguel).order_by(Aluguel.valor.asc())
        else:
            return False

    @staticmethod
    def Listar_Alugueis_Cidade(cidade):
        from database.database import Aluguel, Apartamento, Predio
        return (
            session.query(Aluguel)
            .join(Apartamento, Aluguel.id_apartamento == Apartamento.id)
            .join(Predio, Apartamento.id_predio == Predio.id)
            .filter(Predio.cidade == cidade)
            .all()
        )
        
    @staticmethod
    def Listar_Alugueis_Estado(estado):
        from database.database import Aluguel, Apartamento, Predio
        return (
            session.query(Aluguel)
            .join(Apartamento, Aluguel.id_apartamento == Apartamento.id)
            .join(Predio, Apartamento.id_predio == Predio.id)
            .filter(Predio.estado == estado)
            .all()
        )



        