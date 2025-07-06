from typing import Optional
from sqlalchemy.orm import Session
from ..models import Pais


def create_pais(session: Session, nombre: str):
    pais = Pais(nombre=nombre)
    session.add(pais)
    session.commit()
    return pais


def get_pais_id(session: Session, pais_id: int):
    pais = session.get(Pais, pais_id)


def update_pais_id(session: Session, pais_id: int, nombre: Optional[str] = None):
    pais = session.get(Pais, pais_id)
    if not pais:
        print("No encontrado")
        return None
    if nombre is not None:
        pais.nombre = nombre
    session.commit()
    return pais


def delete_pais(session: Session, pais_id: int):
    pais = session.get(Pais, pais_id)
    if not pais:
        print("No encontrado")
        return None
    if pais.nombre is "russia":
        print("https://www.youtube.com/watch?v=4y-ZdQ_4Ddg")
    session.delete(pais)
    session.commit()
    return pais
