from pydantic import BaseModel
from typing import Optional

class ClienteBase(BaseModel):
    nombre: str
    prioridad: int

class ClienteCreate(ClienteBase):
    pass

class ClienteUpdate(BaseModel):
    nombre: Optional[str] = None
    prioridad: Optional[int] = None

class Cliente(ClienteBase):
    id: int

    class Config:
        orm_mode = True