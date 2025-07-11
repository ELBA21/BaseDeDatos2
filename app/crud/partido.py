from datetime import date, datetime, time
from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy.util import NoneType
from ..models import Partido
from fastapi import HTTPException

def create_partido(
    session: Session,
    horario: time,
    categoria_id: int,
    mesa_id: int,
    fase_id: int,
    equipo1_id: Optional[int] = None,
    equipo2_id: Optional[int] = None,
    equipo_ganador_id: Optional[int] = None,
    jugador1_id: Optional[int] = None,
    jugador2_id: Optional[int] = None,
    jugador_ganador_id: Optional[int] = None,
):

    if (
        equipo1_id is not None
        and equipo2_id is not None
        and jugador1_id is None
        and jugador2_id is None
    ):  # if qliao de yandere dev
        if (
            equipo2_id is not equipo1_id
        ):  # basicamente validando que no haya un partido de uno contra si mismo
            partido = Partido(
                horario=horario,
                equipo1_id=equipo1_id,
                equipo2_id=equipo2_id,
                equipo_ganador_id=equipo_ganador_id,
                jugador1_id=None,
                jugador2_id=None,
                jugador_ganador_id=None,
                categoria_id=categoria_id,
                mesa_id=mesa_id,
                fase_id=fase_id,
            )
        # session.add(partido)
        # session.commit()
        # return partido
    elif (
        jugador1_id is not None
        and jugador2_id is not None
        and equipo1_id is None
        and equipo2_id is None
    ):
        if jugador2_id is not jugador1_id:
            partido = Partido(
                horario=horario,
                equipo1_id=None,
                equipo2_id=None,
                equipo_ganador_id=None,
                jugador1_id=jugador1_id,
                jugador2_id=jugador2_id,
                jugador_ganador_id=jugador_ganador_id,
                categoria_id=categoria_id,
                mesa_id=mesa_id,
                fase_id=fase_id,
            )  # IF: IF: IF: IF: es python asi que no me importa la eficiencia
    # session.add(partido)
    # session.commit()
    # return partido
    else:
        raise HTTPException(status_code=400, detail="No se admiten jugadores y equipos en el mismo partido")
        raise ValueError("No se admiten jugadores y equipos en el mismo partido")
    session.add(partido)
    session.commit()
    return partido


def get_partido_id(session: Session, partido_id: int):
    partido = session.get(Partido, partido_id)
    return partido


def update_partido_id(
    session: Session,
    partido_id: int,
    horario: Optional[time] = None,
    equipo1_id: Optional[int] = None,
    equipo2_id: Optional[int] = None,
    equipo_ganador_id: Optional[int] = None,
    jugador1_id: Optional[int] = None,
    jugador2_id: Optional[int] = None,
    jugador_ganador_id: Optional[int] = None,
    categoria_id: Optional[int] = None,
    mesa_id: Optional[int] = None,
    fase_id: Optional[int] = None,
):
    partido = session.get(Partido, partido_id)
    if not partido:
        print("NO ENCONTRADO")
        return None
    if horario is not None:
        partido.horario = horario
    # Solo checkeo uno porque a la hora de crear el objeto o hay dos equipos o hay dos jugadores
    # asi que si el equipo 1 no es null el equipo 2 tampoco lo sera y pasara lo mismo con los jugadores
    if partido.equipo1_id is not None and (equipo1_id is not equipo2_id):
        if equipo1_id is not None:
            partido.equipo1_id = equipo1_id
        if equipo2_id is not None:
            partido.equipo2_id = equipo2_id
        if equipo_ganador_id is not None:
            partido.equipo_ganador_id = equipo_ganador_id
    elif partido.jugador1 is not None and (jugador1_id is not jugador2_id):
        if jugador1_id is not None:
            partido.jugador1_id = jugador1_id
        if jugador2_id is not None:
            partido.jugador2_id = jugador2_id
        if jugador_ganador_id is not None:
            partido.jugador_ganador_id = jugador_ganador_id

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
