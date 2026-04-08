from sqlalchemy.orm import Session
import models, schemas

#Criar curso
def criar_curso(db: Session, curso: schemas.CursoCreate):
    db_curso = models.Curso(**curso.dict())
    db.add(db_curso)
    db.commit()
    db.refresh(db_curso)
    return db_curso

#Listar curso
def listar_cursos(db: Session, page: int = 1, limit: int = 10):
    query = db.query(models.Curso)

    # Ordena do mais novo pro mais antigo
    query = query.order_by(desc(models.Curso.id))

    return query.offset((page - 1) * limit).limit(limit).all()

#buscar curso por ID
def buscar_curso(db: Session, curso_id: int):
    return db.query(models.Curso).filter(models.Curso.id == curso_id).first()

#Atualizar curso
def atualizar_curso(db: Session, curso_id: int, curso: schemas.CursoUpdate):
    db_curso = buscar_curso(db, curso_id)

    if db_curso:
        db_curso.nome = curso.nome
        db_curso.descricao = curso.descricao
        db.commit()
        db.refresh(db_curso)

    return db_curso

#Deletar curso
def deletar_curso(db: Session, curso_id: int):
    db_curso = buscar_curso(db, curso_id)

    if db_curso:
        db.delete(db_curso)
        db.commit()
    
    return db_curso


#Matricular aluno
def matricular_aluno(db: Session, matricula):
    nova = models.Matricula(
        aluno_id=matricula.aluno_id,
        curso_id=matricula.curso_id
    )
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

#Listar cursos de aluno
def cursosdo_aluno(db: Session, aluno_id: int):
    aluno = db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()
    return aluno.cursos if aluno else []    

 #Listar alunos de um curso   
def alunos_do_curso(db: Session, curso_id: int):
    curso = db.query(models.Curso).filter(models.Curso.id == curso_id).first()
    return curso.alunos if curso else []

#Operação 	Função
#Create =	criar_curso
#Read =	  listar_cursos
#Create =	criar_aluno
#Read =	  listar_alunos