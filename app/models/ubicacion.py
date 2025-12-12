from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Ubicacion(Base):
    __tablename__ = "ubicaciones"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    direccion = Column(String)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), index=True)
    delegacion_id = Column(Integer, ForeignKey("delegaciones.id"), index=True)

    delegacion = relationship("Delegacion", back_populates="ubicaciones")
    tareas = relationship("Tarea", back_populates="ubicacion")