from pydantic import BaseModel, ConfigDict
from typing import Optional

class ORMBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

class Tarea_tecnicoBase(ORMBase):
    tarea_id: int
    tecnico_id: int

class Tarea_tecnicoCreate(Tarea_tecnicoBase):
    pass

class Tarea_tecnicoUpdate(ORMBase):
    tarea_id: Optional[int] = None
    tecnico_id: Optional[int] = None

class Tarea_tecnico(Tarea_tecnicoBase):
    id: int