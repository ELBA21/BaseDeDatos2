from fastapi import APIRouter, Depends, HTTPException
from ..db import get_db
from ..crud.partido import (
    get_partido_id,
    create_partido,
    update_partido_id,
    delete_partido,
)
from sqlalchemy.orm import Session
from typing import Optional
from datetime import date, datetime, time

router = APIRouter()


@router.post("/")
def create_partido_endpoint(
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
    session: Session = Depends(get_db),
):
    partido = create_partido(
        session,
        horario,
        categoria_id,
        mesa_id,
        fase_id,
        equipo1_id,
        equipo2_id,
        equipo_ganador_id,
        jugador1_id,
        jugador2_id,
        jugador_ganador_id,
    )
    return {
        "id": partido.id,
        "horario": partido.horario,
        "equipo1_id": partido.equipo1_id,
        "equipo2_id": partido.equipo2_id,
        "equipo_ganador_id": partido.equipo_ganador_id,
        "jugador1_id": partido.jugador1_id,
        "jugador2_id": partido.jugador2_id,
        "jugador_ganador_id": partido.jugador_ganador_id,
        "categoria_id": partido.categoria_id,
        "mesa_id": partido.mesa_id,
        "fase_id": partido.fase_id,
    }


@router.get("/{partido_id}")
def get_partido_id_endpoint(partido_id: int, session: Session = Depends(get_db)):
    partido = get_partido_id(session, partido_id)
    if not partido:
        raise HTTPException(status_code=404, detail="Partido No Encontrado")
    return {
        "id": partido.id,
        "horario": partido.horario,
        "equipo1_id": partido.equipo1_id,
        "equipo2_id": partido.equipo2_id,
        "equipo_ganador_id": partido.equipo_ganador_id,
        "jugador1_id": partido.jugador1_id,
        "jugador2_id": partido.jugador2_id,
        "jugador_ganador_id": partido.jugador_ganador_id,
        "categoria_id": partido.categoria_id,
        "mesa_id": partido.mesa_id,
        "fase_id": partido.fase_id,
    }


@router.put("/{partido_id}")
def update_partido_id_endpoint(
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
    session: Session = Depends(get_db),
):
    partido = update_partido_id(
        session,
        partido_id,
        horario,
        equipo1_id,
        equipo2_id,
        equipo_ganador_id,
        jugador1_id,
        jugador2_id,
        jugador_ganador_id,
        categoria_id,
        mesa_id,
        fase_id,
    )
    if not partido:
        raise HTTPException(status_code=404, detail="Partido no encontrado")
    return {
        "id": partido.id,
        "horario": partido.horario,
        "equipo1_id": partido.equipo1_id,
        "equipo2_id": partido.equipo2_id,
        "equipo_ganador_id": partido.equipo_ganador_id,
        "jugador1_id": partido.jugador1_id,
        "jugador2_id": partido.jugador2_id,
        "jugador_ganador_id": partido.jugador_ganador_id,
        "categoria_id": partido.categoria_id,
        "mesa_id": partido.mesa_id,
        "fase_id": partido.fase_id,
    }


@router.delete("/{partido_id}")
def delete_partido_endpoint(partido_id: int, session: Session = Depends(get_db)):
    partido = delete_partido(session, partido_id)
    if not partido:
        raise HTTPException(status_code=404, detail="Partido No Encontrado")
    return {
        "id": partido.id,
        "horario": partido.horario,
        "equipo1_id": partido.equipo1_id,
        "equipo2_id": partido.equipo2_id,
        "equipo_ganador_id": partido.equipo_ganador_id,
        "jugador1_id": partido.jugador1_id,
        "jugador2_id": partido.jugador2_id,
        "jugador_ganador_id": partido.jugador_ganador_id,
        "categoria_id": partido.categoria_id,
        "mesa_id": partido.mesa_id,
        "fase_id": partido.fase_id,
    }

