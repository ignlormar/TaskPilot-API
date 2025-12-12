from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Habilidad(Base):
    __tablename__ = "habilidades"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)

    tecnicos = relationship("TecnicoHabilidad", back_populates="habilidad")
    tareas = relationship("TareaHabilidad", back_populates="habilidad")