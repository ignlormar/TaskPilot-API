from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from app.schemas.ubicacion import UbicacionShort


class ORMBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

class ClienteBase(ORMBase):
    nombre: str
    prioridad: int

class ClienteCreate(ClienteBase):
    pass

class ClienteUpdate(ORMBase):
    nombre: Optional[str] = None
    prioridad: Optional[int] = None

class Cliente(ClienteBase):
    id: int
    ubicaciones: List[UbicacionShort] = []