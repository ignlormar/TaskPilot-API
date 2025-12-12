from datetime import datetime, date

from pydantic import BaseModel, ConfigDict
from typing import Optional

class ORMBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

class TareaBase(ORMBase):
    nombre: str
    cliente_id: int
    ubicacion_id: int
    fecha_limite: date
    fecha_asignada: datetime
    tecnicos_requeridos: int

class TareaCreate(TareaBase):
    pass

class TareaUpdate(ORMBase):
    nombre: Optional[str] = None
    cliente_id: Optional[int] = None
    ubicacion_id: Optional[int] = None
    fecha_limite: Optional[date] = None
    fecha_asignada: Optional[datetime] = None
    tecnicos_requeridos: Optional[int] = None

class Tarea(TareaBase):
    id: int