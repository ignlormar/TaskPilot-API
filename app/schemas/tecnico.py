from datetime import time

from pydantic import BaseModel, ConfigDict
from typing import Optional

class ORMBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

class TecnicoBase(ORMBase):
    nombre: str
    delegacion_id: int
    horario_inicio: time
    horario_fin: time

class TecnicoShort(ORMBase):
    nombre: str

class TecnicoCreate(TecnicoBase):
    pass

class TecnicoUpdate(ORMBase):
    nombre: Optional[str] = None
    delegacion_id: Optional[int] = None
    horario_inicio: Optional[time] = None
    horario_fin: Optional[time] = None

class Tecnico(TecnicoBase):
    id: int
