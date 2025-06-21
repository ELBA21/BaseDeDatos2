from datetime import date
from typing import Optional
from sqlalchemy.orm import Session
from ..models import Jugador, Asociacion,Categoria

def create_jugador(session: Session, nombre:str, fecha_nacimiento:date, genero:str, pais:str, ciudad:str, asociacion_id:int, categoria_id:int):
    jugador = Jugador(nombre=nombre, fecha_nacimiento=fecha_nacimiento, genero=genero, pais=pais, ciudad=ciudad, asociacion_id=asociacion_id, categoria_id=categoria_id)
    session.add(jugador)
    session.commit()
    return jugador


def get_jugador_id(session: Session, jugador_id:int):
    jugador = session.get(Jugador, jugador_id)
    return jugador

def update_jugador_id(session: Session, jugador_id:int, nombre:Optional[str]=None, fecha_nacimiento:Optional[date]=None, genero:Optional[str]=None, pais:Optional[str]=None, ciudad:Optional[str]=None, asociacion_id:Optional[int]=None, categoria_id:Optional[int]=None):
    jugador = session.get(Jugador, jugador_id)
    if not jugador:
        print("NO ENCONTRADO")
        return None
    if nombre is not None:
        jugador.nombre = nombre
    if fecha_nacimiento is not None:
        jugador.fecha_nacimiento = fecha_nacimiento
    if genero is not None:
        jugador.genero = genero
    if pais is not None:
        jugador.pais = pais
    if ciudad is not None:
        jugador.ciudad = ciudad
    if asociacion_id is not None:
        jugador.asociacion_id = asociacion_id
    if categoria_id is not None:
        jugador.categoria_id = categoria_id
    session.commit()
    return jugador

def delete_jugador(session: Session, jugador_id:int):
    jugador = session.get(Jugador, jugador_id)
    if not jugador:
        print("NO ENCONTRADO")
        return None
    session.delete(jugador)
    session.commit()
    return jugador