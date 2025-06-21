from datetime import date, datetime, time
from typing import Optional
from sqlalchemy.orm  import Session
from ..models import Partido

def create_partido(session: Session, horario:time, resultado:str, equipo1_id:int, equipo2_id:int, jugador1_id:int, jugador2_id:int, categoria_id:int,mesa_id:int,fase_id:int):
    partido = Partido(horario=horario, resultado=resultado, equipo1_id=equipo1_id, equipo2_id=equipo2_id, jugador1_id=jugador1_id, jugador2_id=jugador2_id, categoria_id=categoria_id, mesa_id=mesa_id, fase_id=fase_id)
    session.add(partido)
    session.commit()
    return partido

def get_partido_id(session: Session, partido_id: int):
    partido = session.get(Partido, partido_id)
    return partido

def update_partido_id(session: Session,partido_id:int, horario: Optional[time] = None, resultado: Optional[str] = None, equipo1_id: Optional[int] = None, equipo2_id: Optional[int] = None, jugador1_id: Optional[int] = None, jugador2_id: Optional[int] = None, categoria_id: Optional[int] = None, mesa_id: Optional[int] = None, fase_id: Optional[int] = None):
    partido = session.get(Partido, partido_id)
    if not partido:
        print("NO ENCONTRADO")
        return None
    if horario is not None:
        partido.horario = horario
    if resultado is not None:
        partido.resultado = resultado
    if equipo1_id is not None:
        partido.equipo1_id = equipo1_id
    if equipo2_id is not None:
        partido.equipo2_id = equipo2_id
    if jugador1_id is not None:
        partido.jugador1_id = jugador1_id
    if jugador2_id is not None:
        partido.jugador2_id = jugador2_id
    if categoria_id is not None:
        partido.categoria_id = categoria_id
    if mesa_id is not None:
        partido.mesa_id = mesa_id
    if fase_id is not None:
        partido.fase_id = fase_id
    session.commit()
    return partido


def delete_partido(session: Session, partido_id: int):
    partido = session.get(Partido, partido_id)
    if not partido:
        print("NO ENCONTRADO")
        return None
    session.delete(partido)
    session.commit()
    return partido