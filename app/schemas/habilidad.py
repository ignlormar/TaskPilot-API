from pydantic import BaseModel, ConfigDict
from typing import Optional

class ORMBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

class HabilidadBase(ORMBase):
    nombre: str

class HabilidadCreate(HabilidadBase):
    pass

class HabilidadUpdate(ORMBase):
    nombre: Optional[str] = None

class Habilidad(HabilidadBase):
    id: int
