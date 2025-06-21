from fastapi  import APIRouter, Depends, HTTPException
from ..db import get_db
from ..crud.equipo import (get_equipo_id, create_equipo, update_equipo_id, delete_equipo)
from sqlalchemy.orm import Session
from typing import Optional
router = APIRouter()

@router.post("/")
def create_equipo_endpoint(nombre: str, jugador_id: int, jugador2_id: int, categoria_id: int, session: Session = Depends(get_db)):
    equipo = create_equipo(session, nombre, jugador_id, jugador2_id, categoria_id)
    return {"id": equipo.id,
            "nombre": equipo.nombre,
            "jugador1": equipo.jugador_id,
            "jugador2": equipo.jugador2_id,
            "categoria": equipo.categoria_id}

@router.get("/{equipo_id}")
def get_equipo_id_endpoint(equipo_id: int, session: Session = Depends(get_db)):
    equipo = get_equipo_id(session, equipo_id)
    if not equipo:
        raise HTTPException(status_code=404, detail="Equipo No Encontrado")
    return {"id": equipo.id,
            "nombre": equipo.nombre,
            "jugador1": equipo.jugador_id,
            "jugador2": equipo.jugador2_id,
            "categoria": equipo.categoria_id}


@router.put("/{equipo_id}")
def update_equipo_id_endpoint(equipo_id: int, nombre: Optional[str] = None, jugador_id: Optional[int] = None, jugador2_id: Optional[int] = None, categoria_id: Optional[int] = None, session: Session = Depends(get_db)):
    equipo = update_equipo_id(session, equipo_id, nombre, jugador_id, jugador2_id, categoria_id)
    if not equipo:
        raise HTTPException(status_code=404, detail="Equipo no encontrado")
    return {"id": equipo.id,
            "nombre": equipo.nombre,
            "jugador1": equipo.jugador_id,
            "jugador2": equipo.jugador2_id,
            "categoria": equipo.categoria_id}

@router.delete("/{equipo_id}")
def delete_equipo_endpoint(equipo_id: int, session: Session = Depends(get_db)):
    equipo = delete_equipo(session, equipo_id)
    if not equipo:
        raise HTTPException(status_code=404, detail="Equipo No encontrado")
    return {"id": equipo.id,
            "nombre": equipo.nombre,
            "jugador1": equipo.jugador_id,
            "jugador2": equipo.jugador2_id,
            "categoria": equipo.categoria_id}