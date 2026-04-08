from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Matricula(Base):
    __tablename__ = "matriculas"

    id = Column(Integer, primary_key=True, index=True)
    aluno_id = Column(Integer, ForeignKey("alunos.id"))
    curso_id = Column(Integer, ForeignKey("cursos.id"))

    status = Column(String, default="ativa")

    aluno = relationship("Aluno", back_populates="matriculas")
    curso = relationship("Curso", back_populates="matriculas")

class Curso(Base):
    __tablename__ = "cursos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    descricao = Column(String)

    alunos = relationship("Aluno", back_populates="curso")


class Aluno(Base):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    idade = Column(Integer)

    curso_id = Column(Integer, ForeignKey("cursos.id"))

    curso = relationship("Curso", back_populates="alunos")

#Aqui criamos relacionamento entre as tabelas 

#CURSO id, idade, descricao

#ALUNOS id, nome, idade, curso_id

