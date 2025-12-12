from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Tarea(Base):
    __tablename__ = "tareas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    ubicacion_id = Column(Integer, ForeignKey("ubicaciones.id"))
    fecha_limite = Column(DateTime)
    fecha_asignada = Column(DateTime)
    tecnicos_requeridos = Column(Integer, nullable=False)

    clientes = relationship("Cliente", back_populates="tareas")
    ubicacion = relationship("Ubicacion", back_populates="tareas")
    habilidades = relationship("TareaHabilidad", back_populates="tarea")
    tecnicos = relationship("TareaTecnico", back_populates="tarea")
