from sqlalchemy import Column, Integer, String, ForeignKey, Time
from .db import Base


class Asociacion(Base):
    __tablename__ = 'Asociacion'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    ciudad = Column(String, nullable=False)
    pais = Column(String, nullable=False)
