from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.database import Base
from database.database_tools import Db_Tools
from datetime import date

if __name__ == "__main__":
    novo_usuario = Db_Tools.Criar_Usuario("Joao","12345678910",date(2025, 6, 4),"123@123.com")
    