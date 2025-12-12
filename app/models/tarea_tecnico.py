from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class TareaTecnico(Base):
    __tablename_ = "tarea_tecnicos"

    id = Column(Integer, primary_key=True, index=True)
    tarea_id = Column(Integer, ForeignKey("tareas.id"))
    tecnico_id = Column(Integer, ForeignKey("tecnicos.id"))

    tarea = relationship("Tarea", back_populates="tecnicos")
    tecnico = relationship("Tecnico", back_populates="tareas")