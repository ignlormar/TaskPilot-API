from pydantic import BaseModel, ConfigDict
from typing import Optional, List

from app.schemas.tecnico import TecnicoShort


class ORMBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

class DelegacionBase(ORMBase):
    nombre: str
    direccion: str

class DelegacionCreate(DelegacionBase):
    pass

class DelegacionUpdate(ORMBase):
    nombre: Optional[str] = None
    direccion: Optional[str] = None

class Delegacion(DelegacionBase):
    id: int
    tecnicos: List[TecnicoShort] = []