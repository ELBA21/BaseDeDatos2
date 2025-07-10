from fastapi import APIRouter, Depends, HTTPException
from ..db import get_db
from ..crud.ciudad import create_ciudad, get_ciudad_id, update_ciudad_id, delete_ciudad
from ..crud.pais import get_pais_id
from sqlalchemy.orm import Session, session
from typing import Optional
from datetime import date


router = APIRouter()


@router.post("/")
def create_ciudad_endpoint(
    nombre: str,
    pais: int,
    session: Session = Depends(get_db),
):
    pais_id = get_pais_id(session, pais)
    if not pais_id:
        raise HTTPException(status_code=404, detail="Pais no encontrado")
    ciudad = create_ciudad(session, nombre, pais)
    return {
        "id": ciudad.id,
        "nombre": ciudad.nombre,
        "pais": ciudad.pais,
    }


@router.get("/{ciudad_id}")
def get_ciudad_id_endpoint(
    ciudad_id: int,
    session: Session = Depends(get_db),
):
    ciudad = get_ciudad_id(session, ciudad_id)
    if not ciudad:
        raise HTTPException(status_code=404, detail="Ciudad no encontrado")
    return {
        "id": ciudad.id,
        "nombre": ciudad.nombre,
        "pais": ciudad.pais,
    }


@router.put("/{ciudad_id}")
def update_ciudad_id_endpoint(
    ciudad_id: int,
    nombre: Optional[str] = None,
    pais: Optional[int] = None,
    session: Session = Depends(get_db),
):
    if pais is not None:
        pais_id = get_pais_id(session, pais)
        if not pais_id:
            raise HTTPException(status_code=404, detail="Pais no encontrado")
    ciudad = update_ciudad_id(session, ciudad_id, nombre, pais)
    if not ciudad:
        raise HTTPException(status_code=404, detail="Ciudad no encontrado")
    return {
        "id": ciudad.id,
        "nombre": ciudad.nombre,
        "pais": ciudad.pais,
    }


@router.delete("/{ciudad_id}")
def delete_ciudad_endpoint(ciudad_id: int, session: Session = Depends(get_db)):
    ciudad = delete_ciudad(session, ciudad_id)
    if not ciudad:
        raise HTTPException(status_code=404, detail="Ciudad no encontrado")
    return {
        "id": ciudad.id,
        "nombre": ciudad.nombre,
        "pais": ciudad.pais,
    }
