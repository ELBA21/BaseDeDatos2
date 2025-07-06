from typing import Optional
from sqlalchemy.orm import Session
from ..models import Ciudad, Pais


def create_ciudad(session: Session, nombre: str, pais: int):
    ciudad = Ciudad(nombre=nombre, pais=pais)
    session.add(ciudad)
    session.commit()
    return ciudad


def get_ciudad_id(session: Session, ciudad_id: int):
    ciudad = session.get(Ciudad, ciudad_id)
    return ciudad


def update_ciudad_id(
    session: Session, ciudad_id: int, nombre: Optional[str], pais: Optional[int]
):
    ciudad = session.get(Ciudad, ciudad_id)
    if not ciudad:
        print("no encontrado")
        return None
    if nombre is not None:
        ciudad.nombre = nombre
    if pais is not None:
        ciudad.pais = pais

    session.commit()
    return ciudad


def delete_ciudad(session: Session, ciudad_id: int):
    ciudad = session.get(Ciudad, ciudad_id)
    if not ciudad:
        print("no encontrado")
        return None
    session.delete(ciudad)
    session.commit()
    return ciudad
