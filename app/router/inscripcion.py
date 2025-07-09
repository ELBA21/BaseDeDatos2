from fastapi import APIRouter, Depends, HTTPException
from ..db import get_db
from ..crud.inscripcion import (
    create_inscripcion,
    delete_inscripcion,
    get_inscripcion_id,
    update_inscripcion_id,
)
from sqlalchemy.orm import Session, session
from typing import Optional

from app.crud import inscripcion

router = APIRouter()


@router.post("/")
def create_inscripcion_endpoint(
    torneo_categoria_id: int,
    jugador_id: Optional[int] = None,
    equipo_id: Optional[int] = None,
    session: Session = Depends(get_db),
):
    if (jugador_id == None and equipo_id == None) or (
        jugador_id != None and equipo_id != None
    ):
        raise HTTPException(
            status_code=400,
            detail="Solo se puede inscribir un equipo o un jugador a la vez",
        )

    if (
        (jugador_id != None and jugador_id < 1)
        or (equipo_id != None and equipo_id < 1)
        or torneo_categoria_id < 1
    ):
        raise HTTPException(
            status_code=400, detail="Necesito un entero positivo, amermelao"
        )

    inscripcion = create_inscripcion(
        session, torneo_categoria_id, jugador_id, equipo_id
    )
    return {
        "id": inscripcion.id,
        "jugador_id": inscripcion.jugador_id,
        "equipo_id": inscripcion.equipo_id,
        "torneo_categoria_id": inscripcion.torneo_categoria_id,
    }


@router.get("/")
def get_inscripcion_id_endpoint(
    inscripcion_id: int,
    session: Session = Depends(get_db),
):
    inscripcion = get_inscripcion_id(session, inscripcion_id)
    if not inscripcion:
        raise HTTPException(status_code=404, detail="No se encontro la inscripcion")
    return {
        "id": inscripcion.id,
        "jugador_id": inscripcion.jugador_id,
        "equipo_id": inscripcion.equipo_id,
        "torneo_categoria_id": inscripcion.torneo_categoria_id,
    }


@router.put("/")
def update_inscripcion_id_endpoint(
    inscripcion_id: int,
    torneo_categoria_id: Optional[int] = None,
    jugador_id: Optional[int] = None,
    equipo_id: Optional[int] = None,
    session: Session = Depends(get_db),
):
    if (jugador_id == None and equipo_id == None) or (
        jugador_id != None and equipo_id != None
    ):
        raise HTTPException(
            status_code=400,
            detail="Solo se puede inscribir un equipo o un jugador a la vez",
        )
    if (
        (jugador_id != None and jugador_id < 1)
        or (equipo_id != None and equipo_id < 1)
        or (torneo_categoria_id is not None and torneo_categoria_id < 1)
    ):
        raise HTTPException(
            status_code=400, detail="Necesito un entero positivo, amermelao"
        )

    inscripcion = update_inscripcion_id(
        session, inscripcion_id, torneo_categoria_id, jugador_id, equipo_id
    )
    if not inscripcion:
        raise HTTPException(status_code=404, detail="No se encontro la inscripcion")
    return {
        "id": inscripcion.id,
        "jugador_id": inscripcion.jugador_id,
        "equipo_id": inscripcion.equipo_id,
        "torneo_categoria_id": inscripcion.torneo_categoria_id,
    }


@router.delete("/")
def delete_inscripcion_endpoint(
    inscripcion_id: int,
    session: Session = Depends(get_db),
):
    inscripcion = delete_inscripcion(session, inscripcion_id)
    if not inscripcion:
        raise HTTPException(status_code=404, detail="No se encontro la inscripcion")
    return {
        "id": inscripcion.id,
        "jugador_id": inscripcion.jugador_id,
        "equipo_id": inscripcion.equipo_id,
        "torneo_categoria_id": inscripcion.torneo_categoria_id,
    }

