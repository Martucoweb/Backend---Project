from sqlalchemy.orm import Session
import models, schemas

#==================
#ALLUNOS - CRUD COMPLETO 
#==================

def criar_aluno(db: Session, aluno: schemas.AlunoCreate):
    novo_aluno = models.Aluno(
    nome=aluno.nome,
    email=aluno.email
    )
    db.add(novo_aluno)
    db.commit()
    db.refresh(novo_aluno)
    return novo_aluno
  
  
  
def listar_alunos(db: Session):
    return db.query(models.Aluno).all()
  
  
  
def buscar_aluno(db: Session, aluno_id: int):
    return db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()    
  
  
def atualizar_aluno(db: Session, aluno_id: int, aluno: schemas.AlunoCreate):
    aluno_db = db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()
    
    if not aluno_db:
        return None
    
    db.delete(aluno_db)
    db.commit()
    return aluno_db
    
    