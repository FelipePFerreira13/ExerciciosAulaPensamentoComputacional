from __future__ import annotations
from typing import List
import os

from sqlalchemy import Column, Integer, DECIMAL, String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, declarative_base, relationship

Base = declarative_base()

class Usuario(Base):

    __tablename__ = 'usuarios'
    id : Mapped[int] = mapped_column(primary_key=True)
    nome = Column(String(100), nullable = False)
    cpf = Column(String(11), nullable = False)
    data_nascimento = Column(Date, nullable = False)
    email = Column(String(100), nullable = False)
    # alugueis: Mapped[List["alugueis"]] = relationship(back_populates="usuario")

class Predio(Base):

    __tablename__ = 'predios'
    id : Mapped[int]= mapped_column(primary_key=True)
    rua = Column(String(100), nullable = False)
    numero = Column(String(10), nullable = False)
    bairro = Column(String(50), nullable = False)
    cidade = Column(String(50), nullable = False)
    estado = Column(String(2), nullable = False)
    # apartamentos: Mapped[List["apartamentos"]] = relationship(back_populates="predio")

class Apartamento(Base):

    __tablename__ = 'apartamentos'
    id : Mapped[int]= mapped_column(primary_key=True)
    id_predio = mapped_column(Integer, ForeignKey("predios.id"), nullable = False)
    numero_apartamento = Column(String(10), nullable = False)
    valor = Column(DECIMAL(11,2), nullable = False)
    # predio: Mapped["predio"] = relationship(back_populates="apartamentos")
    # alugueis: Mapped["alugueis"] = relationship(back_populates="apartamento")
    
class Aluguel(Base):

    __tablename__ = 'alugueis'
    id : Mapped[int]= mapped_column(primary_key=True)
    id_apartamento = mapped_column(Integer, ForeignKey("apartamentos.id"), nullable = False)
    id_usuario = mapped_column(Integer, ForeignKey("usuarios.id"), nullable = False)
    n_semana = Column(Integer, nullable = False)
    valor = Column(DECIMAL(11,2), nullable = False)
    # usuarios: Mapped["usuario"] = relationship(back_populates="alugueis")
    # apartamento: Mapped["apartamento"] = relationship(back_populates="alugueis")

# os.remove("database/database.db")
# engine = create_engine('sqlite:///database/database.db')
# Base.metadata.create_all(engine)