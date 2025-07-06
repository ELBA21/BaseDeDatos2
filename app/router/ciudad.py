from fastapi import APIRouter, Depends, HTTPException
from ..db import get_db
from ..crud.ciudad import create_ciudad, get_ciudad_id, update_ciudad_id, delete_ciudad
from sqlalchemy.orm import Session, session
from typing import Optional
from datetime import date

from app.crud import ciudad

router = APIRouter()


@router.post("/")
def create_ciudad_endpoint(
    nombre: str,
    pais: int,
    session: Session = Depends(get_db),
):
    pais = create_ciudad(session, nombre, pais)
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
        raise HTTPException(status_code=404, detail="Genero no encontrado")
    return {
        "id": ciudad.id,
        "nombre": ciudad.nombre,
        "pais": ciudad.pais,
    }


@router.put("/(ciudad_id)")
def update_ciudad_id_endpoint(
    ciudad_id: int,
    nombre: Optional[str] = None,
    pais: Optional[int] = None,
    session: Session = Depends(get_db),
):
    ciudad = update_ciudad_id(session, ciudad_id, nombre, pais)
    if not ciudad:
        raise HTTPException(status_code=404, detail="Genero no encontrado")
    return {
        "id": ciudad.id,
        "nombre": ciudad.nombre,
        "pais": ciudad.pais,
    }


@router.delete("/{ciudad_id}")
def delete_ciudad_endpoint(ciudad_id: int, session: Session = Depends(get_db)):
    ciudad = delete_ciudad(session, ciudad_id)
    if not ciudad:
        raise HTTPException(status_code=404, detail="Genero no encontrado")
    return {
        "id": ciudad.id,
        "nombre": ciudad.nombre,
        "pais": ciudad.pais,
    }
