from pydantic import BaseModel, ConfigDict
from typing import Optional

class ORMBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

class Tecnico_habilidadBase(ORMBase):
    tecnico_id: int
    habilidad_id: int
    preferencia: int

class Tecnico_habiliddadCreate(Tecnico_habilidadBase):
    pass

class Tecnico_habilidadUpdate(ORMBase):
    tecnico_id: Optional[int] = None
    habilidad_id: Optional[int] = None
    preferencia: Optional[int] = None

class Tecnico_habilidad(Tecnico_habilidadBase):
    id: int