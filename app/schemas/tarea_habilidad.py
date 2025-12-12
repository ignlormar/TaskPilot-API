from pydantic import BaseModel, ConfigDict
from typing import Optional

class ORMBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

class Tarea_habilidadBase(ORMBase):
    tarea_id: int
    habilidad_id: int

class Tarea_habilidadCreate(Tarea_habilidadBase):
    pass

class Tarea_habilidadUpdate(ORMBase):
    tarea_id: Optional[int] = None
    habilidad_id: Optional[int] = None

class Tarea_habilidad(Tarea_habilidadBase):
    id: int