from fastapi import APIRouter, Depends, HTTPException
from ..db import get_db
from ..crud.jugador import (
    get_jugador_id,
    create_jugador,
    update_jugador_id,
    delete_jugador,
)
from sqlalchemy.orm import Session
from typing import Optional
from datetime import date

router = APIRouter()


@router.post("/")
def create_jugador_endpoint(
    nombre: str,
    fecha_nacimiento: date,
    genero: int,
    ciudad: int,
    categoria_id: int,
    asociacion_id: Optional[int] = None,
    session: Session = Depends(get_db),
):
    jugador = create_jugador(
        session,
        nombre,
        fecha_nacimiento,
        genero,
        ciudad,
        categoria_id,
        asociacion_id,
    )
    return {
        "id": jugador.id,
        "nombre": jugador.nombre,
        "fecha_nacimiento": jugador.fecha_nacimiento,
        "genero": jugador.genero,
        "ciudad": jugador.ciudad,
        "asociacion_id": jugador.asociacion_id,
        "categoria_id": jugador.categoria_id,
    }


@router.get("/{jugador_id}")
def get_jugador_id_endpoint(jugador_id: int, session: Session = Depends(get_db)):
    jugador = get_jugador_id(session, jugador_id)
    if not jugador:
        raise HTTPException(status_code=404, detail="Jugador No Encontrado")
    return {
        "id": jugador.id,
        "nombre": jugador.nombre,
        "fecha_nacimiento": jugador.fecha_nacimiento,
        "genero": jugador.genero,
        "ciudad": jugador.ciudad,
        "asociacion_id": jugador.asociacion_id,
        "categoria_id": jugador.categoria_id,
    }


@router.put("/{jugador_id}")
def update_jugador_id_endpoint(
    jugador_id: int,
    nombre: Optional[str] = None,
    fecha_nacimiento: Optional[str] = None,
    genero: Optional[int] = None,
    ciudad: Optional[int] = None,
    asociacion_id: Optional[int] = None,
    categoria_id: Optional[int] = None,
    session: Session = Depends(get_db),
):
    jugador = update_jugador_id(
        session,
        jugador_id,
        nombre,
        fecha_nacimiento,
        genero,
        ciudad,
        asociacion_id,
        categoria_id,
    )
    if not jugador:
        raise HTTPException(status_code=404, detail="Jugador No Encontrado")
    return {
        "id": jugador.id,
        "nombre": jugador.nombre,
        "fecha_nacimiento": jugador.fecha_nacimiento,
        "genero": jugador.genero,
        "ciudad": jugador.ciudad,
        "asociacion_id": jugador.asociacion_id,
        "categoria_id": jugador.categoria_id,
    }


@router.delete("/{jugador_id}")
def delete_jugador_endpoint(jugador_id: int, session: Session = Depends(get_db)):
    jugador = delete_jugador(session, jugador_id)
    if not jugador:
        raise HTTPException(status_code=404, detail="Jugador No Encontrado")
    return {
        "id": jugador.id,
        "nombre": jugador.nombre,
        "fecha_nacimiento": jugador.fecha_nacimiento,
        "genero": jugador.genero,
        "ciudad": jugador.ciudad,
        "asociacion_id": jugador.asociacion_id,
        "categoria_id": jugador.categoria_id,
    }
