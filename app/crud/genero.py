from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import Session
from ..models import Genero


def create_genero(session: Session, nombre: str):
    genero = Genero(nombre=nombre)
    session.add(genero)
    session.commit()
    return genero


# modo WOKE


def get_genero_id(session: Session, genero_id: int):
    genero = session.get(Genero, genero_id)
    return genero


def update_genero_id(
    session: Session,
    genero_id: int,
    nombre: Optional[str] = None,
    #  categoria_id: Optional[int] = None,
):
    genero = session.get(Genero, genero_id)  # no se poque tenemos una
    # funcion que hace esto arriba y hacemos esto pero yo
    # solo estoy siguiendo como lo hicieron mis amiguis
    # -Nurin
    if not genero:
        print("No encontrado, muy woke")
        return None
    if nombre is not None:
        genero.nombre = nombre
    #   if categoria_id is not None:
    #       genero.categoria_id = categoria_id
    session.commit()
    return genero


def delete_genero(session: Session, genero_id: int):
    genero = session.get(Genero, genero_id)
    if not genero:
        print("No encontrado")
        return None  # python como odio q no uses null
    session.delete(genero)
    session.commit()
    return genero
