from pydantic import BaseModel
from typing import Optional

class DelegacionBase(BaseModel):
    nombre: str
    direccion: str

class DelegacionCreate(DelegacionBase):
    pass

class DelegacionUpdate(BaseModel):
    nombre: Optional[str] = None
    direccion: Optional[str] = None

class Delegacion(DelegacionBase):
    id: int

    class Config:
        orm_mode = True