from pydantic import BaseModel, ConfigDict
from typing import Optional

class ORMBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

class UbicacionBase(ORMBase):
    nombre: str
    direccion: str
    cliente_id: int
    delegacion_id: int

class UbicacionShort(ORMBase):
    nombre: str
    direccion: str

class UbicacionCreate(UbicacionBase):
    pass

class UbicacionUpdate(ORMBase):
    nombre: Optional[str] = None
    direccion: Optional[str] = None
    cliente_id: Optional[int] = None
    delegacion_id: Optional[int] = None

class Ubicacion(UbicacionBase):
    id: int