from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class TecnicoHabilidad(Base):
    __table__ = "tecnico_habilidades"

    id = Column(Integer, primary_key=True, index = True)
    tecnico_id = (Integer, ForeignKey("tecnicos.id"))
    habilidad_id = (Integer, ForeignKey("habilidades.id"))
    preferencia = Column(Integer, nullable=False)

    tecnico = relationship("Tecnico", back_populates="habilidades")
    habilidad = relationship("Habilidad", back_populates="tecnicos")