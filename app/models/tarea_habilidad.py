from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class TareaHabilidad(Base):
    __tablename__ = "tarea_habilidades"

    id = Column(Integer, primary_key=True, index=True)
    tarea_id = Column(Integer, ForeignKey("tareas.id"))
    habilidad_id = Column(Integer, ForeignKey("habilidades.id"))

    tarea = relationship("Tarea", back_populates="habilidades")
    habilidad = relationship("Habilidad", back_populates="tareas")