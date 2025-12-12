from sqlalchemy import Column, Integer, String, Time, ForeignKey
from sqlalchemy.orm import relationship
from datetime import time
from app.database import Base

class Tecnico(Base):
    __tablename__ = "tecnicos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    delegacion_id = Column(Integer, ForeignKey("delegaciones.id"))
    horario_inicio = Column(Time, default=time(8, 0))
    horario_fin = Column(Time, default=time(18, 0))

    delegacion = relationship("Delegacion", back_populates="tecnicos")
    habilidades = relationship("TecnicoHabilidad", back_populates="tecnico")
    tareas = relationship("TareaTecnico", back_populates="tecnico")