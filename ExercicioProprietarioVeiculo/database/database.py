from __future__ import annotations
from typing import List

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, declarative_base, relationship

Base = declarative_base()

class Usuario(Base):

    __tablename__ = 'usuario'
    id : Mapped[int] = mapped_column(primary_key=True)
    nome = Column(String(100), nullable = False)
    cpf = Column(String(11), nullable = False)
    carro: Mapped[List["Carro"]] = relationship(back_populates="proprietario")
    caminhao: Mapped[List["Caminhao"]] = relationship(back_populates="proprietario")
    moto: Mapped[List["Moto"]] = relationship(back_populates="proprietario")

class Carro(Base):

    __tablename__ = 'carro'
    id : Mapped[int]= mapped_column(primary_key=True)
    placa = Column(String(8), nullable = False)
    marca = Column(String(50), nullable = False)
    modelo = Column(String(50), nullable = False)
    ano = Column(Integer, nullable = False)
    num_portas = Column(Integer, nullable = False)
    id_proprietario: Mapped[int] = mapped_column(ForeignKey("usuario.id"))
    proprietario: Mapped[List["Usuario"]] = relationship(back_populates="carro")

class Caminhao(Base):

    __tablename__ = 'caminhao'
    id : Mapped[int]= mapped_column(primary_key=True)
    placa = Column(String(8), nullable = False)
    marca = Column(String(50), nullable = False)
    modelo = Column(String(50), nullable = False)
    ano = Column(Integer, nullable = False)
    capacidade_carga = Column(Integer, nullable = False)
    id_proprietario: Mapped[int] = mapped_column(ForeignKey("usuario.id"))
    proprietario: Mapped[List["Usuario"]] = relationship(back_populates="caminhao")

class Moto(Base):

    __tablename__ = 'moto'
    id : Mapped[int]= mapped_column(primary_key=True)
    placa = Column(String(8), nullable = False)
    marca = Column(String(50), nullable = False)
    modelo = Column(String(50), nullable = False)
    ano = Column(Integer, nullable = False)
    cilindrada = Column(Integer, nullable = False)
    id_proprietario: Mapped[int] = mapped_column(ForeignKey("usuario.id"))
    proprietario: Mapped[List["Usuario"]] = relationship(back_populates="moto")
