from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Usuario, Base
from datetime import date

engine = create_engine('sqlite:///database/database.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

class Db_Tools:
    
    def Criar_Usuario(nome: str, cpf: str, data_nascimento: date, email: str) -> Usuario:
        
        novo_usuario = Usuario(nome=nome, cpf=cpf, data_nascimento=data_nascimento, email=email)
        
        session.add(novo_usuario)
        session.commit()
        return novo_usuario
    
