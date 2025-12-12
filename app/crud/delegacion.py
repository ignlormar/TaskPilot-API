from sqlalchemy.orm import Session, selectinload
from app.models.delegacion import Delegacion as DelegacionModel
from app.schemas.delegacion import DelegacionCreate, DelegacionUpdate

def get_delegacion(db: Session, delegacion_id: int):
    return db.query(DelegacionModel).filter(DelegacionModel.id == delegacion_id).options(
        selectinload(DelegacionModel.tecnicos)
    ).first

def get_delegaciones(db: Session):
    return db.query(DelegacionModel).all()

def create_delegacion(db: Session, delegacion: DelegacionCreate):
    db_delegacion = DelegacionModel(**delegacion.model_dump())
    db.add(db_delegacion)
    db.commit()
    db.refresh(db_delegacion)
    return db_delegacion

def update_delegacion(db: Session, db_delegacion: DelegacionModel, update_data: DelegacionUpdate):
    for field, value in update_data.model_dump(exclude_unset=True).items():
        setattr(db_delegacion, field, value)

    db.commit()
    db.refresh(db_delegacion)
    return db_delegacion

def delete_delegacion(db: Session, delegacion_id: int):
    db_delegacion = db.query(DelegacionModel).filter(DelegacionModel.id == delegacion_id).first()
    if db_delegacion:
        db.delete(db_delegacion)
        db.commit()

    return db_delegacion