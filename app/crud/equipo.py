from typing import Optional
from sqlalchemy.orm import Session
from ..models import Equipo
from fastapi import HTTPException

def create_equipo(session: Session,nombre:str,jugador_id:int,jugador2_id:int,categoria_id:int):
    equipo = Equipo(nombre=nombre, jugador_id=jugador_id, jugador2_id=jugador2_id, categoria_id=categoria_id)
    if jugador_id ==  jugador2_id:
        raise HTTPException(status_code = 400,detail="No se puede ingresar el mismo jugador 2 veces" )
    session.add(equipo)
    session.commit()
    return equipo

def get_equipo_id(session:Session, equipo_id:int):
    equipo = session.get(Equipo, equipo_id)
    return equipo

def update_equipo_id(session: Session, equipo_id: int, nombre: Optional[str] = None, jugador_id: Optional[int] = None, jugador2_id: Optional[int] = None, categoria_id: Optional[int] = None):
    equipo = session.get(Equipo, equipo_id)
    if not equipo:
        print("NO ENCONTRADO")
        return None
    if jugador2_id == jugador_id:
        raise HTTPException(status_code=400,detail="No se puede ingresar el mismo jugador 2 veces")
    if nombre is not None:
        equipo.nombre = nombre
    else:
        print("No se insserto nombre")
    if jugador_id is not None:
        equipo.jugador_id = jugador_id
    else:
        print("No se ha insertado jugador1")
    if jugador2_id is not None:
        equipo.jugador2_id = jugador2_id
    else:
        print("No se ha insertado jugador2")
    if categoria_id is not None:
        equipo.categoria_id = categoria_id
    else:
        print("No se ha insertado categoria")
    session.commit()
    return equipo

def delete_equipo(session: Session, equipo_id: int):
    equipo = session.get(Equipo, equipo_id)
    if not equipo:
        print("NO ENCONTRADO")
        return None
    session.delete(equipo)
    session.commit()
    return equipo

