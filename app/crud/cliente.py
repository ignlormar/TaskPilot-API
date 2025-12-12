from sqlalchemy.orm import Session, selectinload
from app.models.cliente import Cliente as ClienteModel
from app.schemas.cliente import ClienteCreate, ClienteUpdate


def get_cliente(db: Session, cliente_id: int):
    return db.query(ClienteModel).filter(ClienteModel.id == cliente_id).options(
        selectinload(ClienteModel.ubicaciones)
    ).first()

def get_clientes(db: Session, skip: int = 0, limit: int = 0):
    return db.query(ClienteModel).offset(skip).limit(limit).all()

def create_cliente(db: Session, cliente: ClienteCreate):
    db_cliente = ClienteModel(**cliente.model_dump())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

def update_cliente(db: Session, db_cliente: ClienteModel, update_data: ClienteUpdate):
    for field, value in update_data.model_dump(exclude_unset=True).items():
        setattr(db_cliente, field, value)

    db.commit()
    db.refresh(db_cliente)
    return db_cliente

def delete_cliente(db: Session, cliente_id: int):
    db_cliente = db.query(ClienteModel).filter(ClienteModel.id == cliente_id).first()
    if db_cliente:
        db.delete(db_cliente)
        db.commit()

    return db_cliente