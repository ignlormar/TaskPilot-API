from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.base import Base

class Delegacion(Base):
    __tablename__ = "delegaciones"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, nullable=False)
    direccion = Column(String, nullable=False)

    tecnicos = relationship("Tecnico", back_populates="delegacion")
    ubicaciones = relationship("Ubicacion", back_populates="delegacion")

