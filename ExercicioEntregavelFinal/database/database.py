from __future__ import annotations
from typing import List
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
    alugueis: Mapped[List["Aluguel"]] = relationship(back_populates="usuarios")
    

class Predio(Base):

    __tablename__ = 'predios'
    id : Mapped[int]= mapped_column(primary_key=True)
    rua = Column(String(100), nullable = False)
    numero = Column(String(10), nullable = False)
    bairro = Column(String(50), nullable = False)
    cidade = Column(String(50), nullable = False)
    estado = Column(String(2), nullable = False)
    apartamentos: Mapped[List["Apartamento"]] = relationship(back_populates="predio")

class Apartamento(Base):

    __tablename__ = 'apartamentos'
    id : Mapped[int]= mapped_column(primary_key=True)
    id_predio = Column(Integer, ForeignKey('predios.id'))
    numero_apartamento = Column(String(10), nullable = False)
    valor = Column(DECIMAL(10, 2), nullable = False)
    link_google = Column(String(512), nullable=True)

    predio = relationship("Predio")
    alugueis: Mapped["Aluguel"] = relationship(back_populates="apartamento")
    
class Aluguel(Base):

    __tablename__ = 'alugueis'
    id : Mapped[int]= mapped_column(primary_key=True)
    id_apartamento = mapped_column(Integer, ForeignKey("apartamentos.id"), nullable = False)
    id_usuario = mapped_column(Integer, ForeignKey("usuarios.id"), nullable = False)
    n_semana = Column(Integer, nullable = False)
    valor = Column(DECIMAL(11,2), nullable = False)
    usuarios: Mapped["Usuario"] = relationship(back_populates="alugueis")
    apartamento: Mapped["Apartamento"] = relationship(back_populates="alugueis")