from sqlalchemy.orm import Session
from app.models.habilidad import Habilidad as HabilidadModel
from app.schemas.habilidad import HabilidadCreate, HabilidadUpdate

def get_habilidades(db: Session):
    return db.query(HabilidadModel).all()

def create_habilidad(db: Session, habilidad: HabilidadCreate):
    db_habilidad = HabilidadModel(**habilidad.model_dump())
    db.add(db_habilidad)
    db.commit()
    db.refresh(db_habilidad)
    return db_habilidad

def update_habilidad(db: Session, db_habilidad: HabilidadModel, update_data: HabilidadUpdate):
    for field, value in update_data.model_dump(exclude_unset=True).items():
        setattr(db_habilidad, field, value)

    db.commit()
    db.refresh(db_habilidad)
    return db_habilidad

def delete_habilidad(db: Session, habilidad_id: int):
    db_habilidad = db.query(HabilidadModel).filter(HabilidadModel.id == habilidad_id).first
    if db_habilidad:
        db.delete(db_habilidad)
        db.commit()

    return db_habilidad