from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import controllers.matriculas_controller as controller
import schemas

router = APIRouter(prefix="/matriculas", tags=["Matrículas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def matricular(matricula: schemas.MatriculaCreate, db: Session = Depends(get_db)):
    return controller.matricular(db, matricula)